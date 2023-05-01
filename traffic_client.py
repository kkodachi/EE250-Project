import requests, config
from typing import Dict
import datetime

# Inspired by Lab 3's API portion
SERVER = 'https://localhost:5000'

# get API url & API key
URL = "https://router.hereapi.com/v8/routes"
API_KEY = config.api_key

def get_traffic(start_lat, start_long, dest_lat, dest_long, formatted_date) -> Dict:
    start = start_lat + ',' + start_long
    destination = dest_lat + ',' + dest_long
    date = datetime.datetime.now()
    param = {"transportMode": "car", 
             "origin": start, 
             "destination": destination, 
             "return": "summary", 
             "departureTime": formatted_date,
             "apikey": API_KEY}
    res = requests.get(URL, params=param)
    return res.json()

def seconds_to_minutes():
    pass

def main():
    # get user input
    dest_lat = input("Enter destination latitude: ")
    dest_long = input("Enter destination longitude: ")
    start_lat = input("Enter starting location latitude: ")
    start_long = input("Enter starting location longitude: ")

    for hr in range(1, 25):
        formatted_date = date.strftime("%Y-%m-%d")
        date = datetime.datetime.strptime(formatted_date, "%Y-%m-%d")

        date_week_before = date - datetime.timedelta(days=7)
        formatted_date = date_week_before.strftime("%Y-%m-%d")

        if (hr <= 9):
            formatted_date += 'T' + '0' + str(hr) + '00:00-08:00'
        else:
            formatted_date += 'T' + str(hr) + '00:00-08:00'
        traffic_data = get_traffic(dest_lat, dest_long, start_lat, start_long,formatted_date)
        response = requests.post(f'{SERVER}/traffic', json=traffic_data)

if __name__ == "__main__":
    main()
