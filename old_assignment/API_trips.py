import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from get_abb import verkorting_station

def get_trip(departure, arrival, time, boolean):
    key1 = '1f11dc707bbd450cbcd02d643dfd4ec4'
    key2 = '07975501f3ff42a5945acdd2193d0cfa'

    headers = {
        'Ocp-Apim-Subscription-Key': key1,
    }

    departure = verkorting_station(departure)
    arrival = verkorting_station(arrival)

    if arrival == 0 or departure == 0:
        print("This station is not known in our database")
        return 1

    # parameters used for request 
    params = urllib.parse.urlencode({
        'dateTime': time,
        'searchForArrival': boolean,
        'lang': 'nl',
        'passing': 'true',
        'fromStation': departure,
        'toStation': arrival,
    })

    try:
        # get response from API
        conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
        conn.request("GET", "/reisinformatie-api/api/v3/trips?%s" % params, "{body}", headers)
        response = conn.getresponse()

        # bytes object to dict
        string = response.read().decode('utf-8')
        json_obj = json.loads(string)

        # get the time from the dict 
        ranking_words = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth']
        for number, legs in enumerate(json_obj['trips'][0]['legs']):
            origin = legs["origin"]["name"]
            time = legs["origin"]["plannedDateTime"]
            direction = legs['direction']
            destination = legs["destination"]["name"]
            time_arrival = legs["destination"]["plannedDateTime"]

            print(
                f'Your {ranking_words[number]} train leaves from {origin}'
                f' in the direction of {direction} at {time[11:16]}.'
                f' You have to get out in {destination} at {time_arrival[11:16]}.'
            )

        conn.close()
    except:
        print("somehting went wrong...")

        return 1
    
    return 0