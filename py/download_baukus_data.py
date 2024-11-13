# Downloading GLORYS for use with fish-quality control work


# Downloading Glorys for Northeast US
# Using Copernicus Marine Toolbox python API

# For Constructing Last day of the month
import datetime
import calendar
import copernicusmarine
import os
import numpy as np


# Access the catalog
catalog = copernicusmarine.describe(overwrite_metadata_cache=True)

# # Log in using credentials: 
# copernicusmarine.login()

# Check directory
os.listdir()

# Variables:
# thetao = potential temperature in C
# so = Salinity in psu
# uo = Eastward ocean current velocity
# vo = Northward ocean current velocity



#############  Downloading from Interim Dataset  #############

# Download the rang of dates from the interim dataset
# Load some years
years = np.arange(2023, 2025)
months = np.arange(1,13)
months = [f"{mnth:02}" for mnth in months]

# Loop through them all
for yr in years:
    for mnth in months:

        # Make a stupid end datetime that adapts to the days in each month
        last_day = datetime.datetime(yr, int(f"{mnth}"), calendar.monthrange(yr, int(f"{mnth}"))[1], 23, 59, 59)

        # Download all the months
        copernicusmarine.subset(
        dataset_id = "cmems_mod_glo_phy_myint_0.083deg_P1D-m",
        variables = ["thetao"],
        minimum_longitude = -72,
        maximum_longitude = -66,
        minimum_latitude = 40,
        maximum_latitude = 46,
        start_datetime = f"{yr}-{mnth}-01T00:00:00",
        end_datetime = last_day.strftime('%Y-%m-%dT%H:%M:%S'),
        minimum_depth = 0,
        maximum_depth = 2000,
        output_filename = f"CMEMS_Northeast_TempSal_{yr}_{mnth}.nc",
        output_directory = "Baukus_GLORYS_data", 
        force_download = True
        )



