import cdsapi

dataset = "reanalysis-era5-single-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": ["mean_sea_level_pressure"],
    "year": ["2025"],
    "month": ["12"],
    "day": [
        "05", "06", "07",
        "08", "09", "10",
        "11", "12", "13"
    ],
    "time": [
        "00:00", "03:00", "06:00",
        "09:00", "12:00", "15:00",
        "18:00", "21:00"
    ],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [-10, -65, -60, -25]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()

