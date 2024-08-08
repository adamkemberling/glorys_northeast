# Northeast US Continental Shelf GLORYS 

Using Copernicus marine toolbox to download GLORYs ocean reanalysis data
for the Northeast US. This repository documents the coede used for building the
local inventory for Northeast US applications.

Glorys Data for the northeast data was downloaded by month using the following options with the Copernicus Marine Toolbox python API:

```
copernicusmarine.subset(
  # 1993-01 through 2012-06
  dataset_id = "cmems_mod_glo_phy_my_0.083deg_P1D-m",
  # 2021-07 through 2023-12
  # dataset_id = "cmems_mod_glo_phy_myint_0.083deg_P1D-m",
  variables = ["thetao", "so"],
  minimum_longitude = -75.7,
  maximum_longitude = -56.9,
  minimum_latitude = 35.2,
  maximum_latitude = 46.2,
  start_datetime = f"{yr}-{mnth}-01T00:00:00",
  end_datetime = last_day.strftime('%Y-%m-%dT%H:%M:%S'),
  minimum_depth = 0,
  maximum_depth = 1500,
  output_filename = f"CMEMS_Northeast_TempSal_{yr}_{mnth}.nc",
  output_directory = "GLORYS_data", 
  force_download = True)
```

`{yr}` & `{mnth}` are loop indices, and `last_day` is generated to be the last datetime for that month.
