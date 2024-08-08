#### Regional Timeseries Check


# Loading/Separating Lobster-ECOL Spatial Areas

#### Libraries
library(gmRi)
library(here)
library(sf)
library(tidyverse)

# Paths to files
poly_paths <- cs_path("mills", "Projects/Lobster ECOL/Spatial_Defs")


#### Separate Shapes for Easier Paralell Workflow  ####
# i'm still bad at python so loops are easier this way

# Load Shapefiles
inshore_areas <- read_sf(str_c(poly_paths, "12nm_poly_statarea/12nm_poly_statarea.shp"))
offshore_areas <- read_sf(str_c(poly_paths, "offshore_sne_gom_dissolve/offshore_sne_gom_dissolve.shp"))

plot(offshore_areas$geometry)



####  Load and Check Regionally Masked Timeseries  ####


# Load CSV files of timeseries

# inshore
inshore_timeseries <- map_dfr(
  setNames(
    list.files(here::here("local_data/inshore_timeseries"), full.names = T), 
    str_remove_all(str_remove_all(list.files(here::here("local_data/inshore_timeseries")), "GLORYs_surfbottemp_"), ".csv")),
  ~read_csv(.x) %>% select(-`...1`), 
  .id = "area_id")

# plot
ggplot(inshore_timeseries) +
  geom_line(aes(time, surface_temp)) +
  facet_wrap(~area_id)


# offshore
offshore_timeseries <- map_dfr(
  setNames(
    list.files(here::here("local_data/offshore_timeseries"), full.names = T), 
    str_remove_all(str_remove_all(list.files(here::here("local_data/offshore_timeseries")), "GLORYs_surfbottemp_"), ".csv")),
  ~read_csv(.x) %>% select(-`...1`), 
  .id = "area_id")

# Plot
ggplot(offshore_timeseries) +
  geom_line(aes(time, surface_temp, color = "Surface Temp")) +
  geom_line(aes(time, bottom_temp, color = "Bottom Temp")) +
  facet_wrap(~area_id, nrow = 2)


offshore_timeseries %>% 
  filter(lubridate::year(time) %in% c(2020, 2021, 2022)) %>% 
  ggplot() +
  geom_line(aes(time, surface_temp, color = "Surface Temp")) +
  geom_line(aes(time, bottom_temp, color = "Bottom Temp"))


