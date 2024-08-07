# Extracting bottom layer
# Recode of work done by Matt Dzaugis used initially for CMIP6
# Use to extract bottom-layer indices (deepest non-NA depth indices)



####  Libraries  ####
import xarray as xr
import os
import numpy as np


# # Move up a directory to access local project files
# os.chdir("..")


# find bottom temp for any netcdf with depth
def find_deepest_depth_indices(ds, variable_id, y_coord, x_coord, depth_coord, maxDepth = 2000):


    # Subset up to an optional max depth
    kwargs = {depth_coord: slice(0, maxDepth)}
    bottom_400 = ds.sel(**kwargs)

    # First get the vertical True/False of valid values
    idx = bottom_400[variable_id].isel(time=0).isnull()
    idx_vals = idx.values


    if len(bottom_400[variable_id][x_coord].dims) == 2:
        multiIndex = True
    else:
        multiIndex = False

    if multiIndex == True:
        dims0 = bottom_400[y_coord].dims[0]
        dims1 = bottom_400[y_coord].dims[1]
    else:
        dims0 = y_coord
        dims1 = x_coord


    # Create the initial final array to store indices (integer type)
    depth_indices = np.zeros((len(idx[y_coord][dims0]), len(idx[x_coord][dims1]))).astype(int)

    # Now find the deepest depth where values are True and store in indices array
    for i in range(len(bottom_400[dims1].values)):
        for j in range(len(bottom_400[dims0].values)):
            located = np.where(idx_vals[:, j, i] == False)
            try:
                depth_indices[j, i] = int(located[-1][-1])
            except IndexError:
                depth_indices[j, i] = 1

    # Gather as a DataArray
    ind = xr.DataArray(depth_indices, dims=[dims0, dims1])

    return ind


#### TESTING  ####
# Apply to glorys downloads: 
# Follow this pattern: https://github.com/adamkemberling/sdm_workflow/blob/main/CMIP6_processing/GetBottomLayer.py

# Test on one file
# Open a file to explore
glorys_93 = xr.open_dataset("GLORYS_data/CMEMS_Northeast_TempSal_1993_01.nc")
glorys_93.variables

# Pull the bottom indices
glorys_bottom_idx = find_deepest_depth_indices(
    ds = glorys_93, 
    variable_id = 'thetao', 
    x_coord = 'longitude', 
    y_coord = 'latitude', 
    depth_coord = 'depth', 
    maxDepth = 1600)



# Use that to extract the variables we care about

# use kwargs to pull values for those indices
kwdepth = {'depth': glorys_bottom_idx}
var_array = glorys_93['thetao']


# Now index the values out
dsSel = var_array.isel(**kwdepth)
ds = dsSel.to_dataset()
ds.thetao.isel(time = 0).plot()




### Test them all:
# Use xr.open_mfdataset() to load all the downloads. 

# Pull the bottom layer and resave. Add another variable indication the depth used **