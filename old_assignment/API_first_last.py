import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from get_abb import verkorting_station
from API_trips import get_trip

"""
Deze werkt alleen als de datum wordt gegeven als YYYY-MM-DD, moet even gezegd worden tegen
de gebruiker
"""

def change_time_first(time):
    suitable_time = time + 'T06:00:00.00Z'
    return suitable_time

def change_time_last(time):
    suitable_time = time + 'T03:00:00.00Z'
    return suitable_time

def get_first_train(departure, arrival, time, boolean):
    print(f"This is the trip advice for the first train from {departure} to {arrival}")
    time = change_time_first(time)
    get_trip(departure, arrival, time, boolean)

    return

def get_last_train(departure, arrival, time, boolean):
    print(f"This is the trip advice for the last train from {departure} to {arrival}")
    time = change_time_last(time)
    get_trip(departure, arrival, time, boolean)

    return