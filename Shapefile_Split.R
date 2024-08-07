# Loading/Separating Lobster-ECOL Spatial Areas

#### Libraries
library(gmRi)
library(here)
library(sf)
library(tidyverse)

# Paths to files
poly_paths <- cs_path("mills", "Projects/Lobster ECOL/Spatial_Defs")


# Load Shapefiles
inshore_areas <- read_sf(str_c(poly_paths, "12nm_poly_statarea/12nm_poly_statarea.shp"))
offshore_areas <- read_sf(str_c(poly_paths, "offshore_sne_gom_dissolve/offshore_sne_gom_dissolve.shp"))


# Check them out/resave:
inshore_areas %>% 
  mutate(area_id = str_c(Id_1, "-", str_replace_all(SHORT_NAME, " ", "_")), .before = "Join_Count") %>% 
  split(.$area_id) %>% 
  imap(~st_write(.x, str_c(poly_paths, "inshore_areas/", .y, ".geojson")))
  #imap(~print(str_c(poly_paths, "inshore_areas/", .y, ".geojson")))


offshore_areas %>% 
  split(.$Region) %>% 
  imap(~st_write(.x, str_c(poly_paths, "offshore_areas/", .y, ".geojson")))
  # imap(~print(str_c(poly_paths, "offshore_areas/", .y, ".geojson")))
