"""
ipwgml.definitions
==================

This module defines shared attributes for the ipwgml package.
"""

ANCILLARY_VARIABLES = [
    "wet_bulb_temperature",
    "two_meter_temperature",
    "lapse_rate",
    "total_column_water_vapor",
    "surface_temperature",
    "moisture_convergence",
    "leaf_area_index",
    "snow_depth",
    "orographic_wind",
    "10m_wind",
    # "surface_type",
    # "mountain_type",
    "land_fraction",
    "ice_fraction",
    "quality_flag",
    "sunglint_angle",
    "airlifting_index",
]

N_CLASSES = {
    "surface_type": 18,
}


ALL_INPUTS = ["gmi", "geo", "geo_ir", "ancillary"]

REFERENCE_SENSORS = ["gmi"]
GEOMETRIES = ["gridded", "on_swath"]
SPLITS = ["training", "validation", "testing", "evaluation"]
SIZES = ["xs", "s", "m", "l", "xl"]
DOMAINS = ["austria", "conus", "korea"]
