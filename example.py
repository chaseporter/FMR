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
