from django.shortcuts import render
import requests
import pandas as pd
from django.http import JsonResponse
from rest_framework.decorators import api_view

# OpenRouteService API Key
ORS_API_KEY = "5b3ce3597851110001cf62480a6673e1ecd4446e9a5316d2f8151946"
ORS_BASE_URL = "https://api.openrouteservice.org/v2/directions/driving-car"

# Load fuel price data
fuel_data = pd.read_csv("fuel-prices-for-be-assessment.csv")

@api_view(['POST'])
def get_route(request):
    data = request.data
    start = data.get("start")
    finish = data.get("finish")
    
    if not start or not finish:
        return JsonResponse({"error": "Missing start or finish location"}, status=400)

    # Fetch route from OpenRouteService
    route_response = requests.post(
        ORS_BASE_URL,
        json={
            "coordinates": [start.split(","), finish.split(",")],
            "profile": "driving-car",
            "format": "json",
            "instructions": True
        },
        headers={"Authorization": ORS_API_KEY, "Content-Type": "application/json"}
    )

    if route_response.status_code != 200:
        return JsonResponse({"error": "Failed to fetch route"}, status=500)

    route_data = route_response.json()

    # Extract total distance in miles
    total_distance = route_data["routes"][0]["summary"]["distance"] / 1609  # meters to miles

    # Fuel calculations
    max_range = 500  # miles per tank
    miles_per_gallon = 10
    gallons_needed = total_distance / miles_per_gallon

    # Finding optimal fuel stops
    stops = []
    current_miles = 0
    while current_miles < total_distance:
        current_miles += max_range
        nearest_stop = fuel_data.iloc[(fuel_data['Retail Price'].idxmin())]  # Cheapest fuel
        stops.append({
            "name": nearest_stop["Truckstop Name"],
            "location": f"{nearest_stop['City']}, {nearest_stop['State']}",
            "price_per_gallon": nearest_stop["Retail Price"]
        })

    # Calculate total fuel cost
    total_fuel_cost = sum(stop["price_per_gallon"] for stop in stops) * (gallons_needed / len(stops))

    return JsonResponse({
        "route": route_data,
        "fuel_stops": stops,
        "total_fuel_cost": total_fuel_cost
    })

