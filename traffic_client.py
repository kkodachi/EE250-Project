import requests, config
from typing import Dict
import datetime, json
from PIL import Image
from io import BytesIO

# Inspired by Lab 3's API portion
SERVER = 'http://172.20.10.3:5000'

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

def main():
    # get user input
    dest_lat = input("Enter destination latitude: ")
    dest_long = input("Enter destination longitude: ")
    start_lat = input("Enter starting location latitude: ")
    start_long = input("Enter starting location longitude: ")

    durations = []
    for hr in range(1, 24):
        now = datetime.datetime.now()
        formatted_date = now.strftime("%Y-%m-%d")
        date = datetime.datetime.strptime(formatted_date, "%Y-%m-%d")

        date_week_before = date - datetime.timedelta(days=7)
        formatted_date = date_week_before.strftime("%Y-%m-%d")

        if (hr <= 9):
            formatted_date += 'T' + '0' + str(hr) + ':00:00-08:00'
        else:
            formatted_date += 'T' + str(hr) + ':00:00-08:00'

        traffic_data = get_traffic(dest_lat, dest_long, start_lat, start_long,formatted_date)

        # access the "duration" at certain hr
        curr_duration = traffic_data['routes'][0]['sections'][0]['summary']['duration']
        durations.append(round(curr_duration / 60, 2))

    response = requests.post(f'{SERVER}/traffic', json=durations)

    # decode the response as a PNG image
    img = Image.open(BytesIO(response.content))

    # display the image
    img.show()

if __name__ == "__main__":
    main()
