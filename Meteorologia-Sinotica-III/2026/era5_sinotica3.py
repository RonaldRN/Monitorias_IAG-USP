import cdsapi

dataset = "reanalysis-era5-pressure-levels"
request = {
    "product_type": ["reanalysis"],
    "variable": [
        "geopotential",
        "specific_humidity",
        "temperature",
        "u_component_of_wind",
        "v_component_of_wind",
        "vertical_velocity"
    ],
    "year": ["2025"],
    "month": ["12"],
    "day": [
        #"05","06","07"
        #"08", "09", "10"
        "11", "12", "13"
    ],
    "time": [
        "00:00", "03:00", "06:00", 
        "09:00", "12:00", "15:00", 
        "18:00", "21:00" 
    ],
    "pressure_level": [
        "1", "2", "3",
        "5", "7", "10",
        "20", "30", "50",
        "70", "100", "125",
        "150", "175", "200",
        "225", "250", "300",
        "350", "400", "450",
        "500", "550", "600",
        "650", "700", "750",
        "800", "850", "900",
        "925", "950", "1000"
    ],
    "data_format": "netcdf",
    "download_format": "unarchived",
    "area": [-10, -65, -60, -25]
}

client = cdsapi.Client()
client.retrieve(dataset, request).download()

