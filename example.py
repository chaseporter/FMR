import fems_api as fems_api

if __name__ == "__main__":
    fuel_params = {
        "startDate": "2025-08-17T00:00:00+00",
        "endDate": "2025-08-18T00:00:00+00",
        "siteId": 1498,
        "fuelType": "Pinegrass",
    }
    fems_results = fems_api.get_fuel_data(fuel_params)
    print(fems_results)

    multiple_fuels_params = {
        "startDate": "2025-08-17T00:00:00+00",
        "endDate": "2025-08-18T00:00:00+00",
        "siteIds": [1498],
        "fuelTypes": ["Pinegrass", "1000-Hour"],
    }
    multiple_fuels_and_sites_results = fems_api.get_fuel_data_of_sites(
        multiple_fuels_params
    )
    print(multiple_fuels_and_sites_results)

    sample_polygon = [
        {"latitude": 48.5, "longitude": -120.7},
        {"latitude": 49.0, "longitude": -120.7},
        {"latitude": 49.0, "longitude": -119.9},
        {"latitude": 48.5, "longitude": -119.9},
    ]
    filtered_sites = fems_api.get_sites_in_polygon(sample_polygon)
    print(filtered_sites)
