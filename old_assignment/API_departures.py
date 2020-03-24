import http.client, urllib.request, urllib.parse, urllib.error, base64
import json
from get_abb import verkorting_station

def get_departures(station):
    key1 = '1f11dc707bbd450cbcd02d643dfd4ec4'
    key2 = '07975501f3ff42a5945acdd2193d0cfa'

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': key1,
    }
    afk_station = verkorting_station(station)

    if afk_station == 0:
        print("This station is not known in our database")
        return 1

    params = urllib.parse.urlencode({
        # Request parameters
        'maxJourneys': '25',
        'lang': 'nl',
        'station': afk_station,
    })
    try:
        # get info from API
        conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
        conn.request("GET", "/reisinformatie-api/api/v2/departures?%s" % params, "{body}", headers)
        response = conn.getresponse()

        # bytes object to dict
        string = response.read().decode('utf-8')
        json_obj = json.loads(string)

        print(f"The following trains leave in the next hour from {station}")
        for element in json_obj['payload']['departures']:
            type_train = element['product']['longCategoryName']
            direction = element['direction']
            track = element['plannedTrack']
            time = element['plannedDateTime'][11:16]
            print(f'The {type_train} to {direction} departs from track'
            f' {track} at {time}')

        conn.close()
    except:
        print("Something went wrong...")
        return 1
    
    return 0 

def get_arrivals(station):
    key1 = '1f11dc707bbd450cbcd02d643dfd4ec4'
    key2 = '07975501f3ff42a5945acdd2193d0cfa'

    headers = {
        # Request headers
        'Ocp-Apim-Subscription-Key': key1,
    }
    afk_station = verkorting_station(station)

    if afk_station == 0:
        print("This station is not known in our database")
        return 1

    params = urllib.parse.urlencode({
        # Request parameters
        'maxJourneys': '25',
        'lang': 'nl',
        'station': afk_station,
    })

    try:
        # get info from API
        conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
        conn.request("GET", "/reisinformatie-api/api/v2/arrivals?%s" % params, "{body}", headers)
        response = conn.getresponse()

        # bytes object to dict
        string = response.read().decode('utf-8')
        json_obj = json.loads(string)

        print(f"The following trains arrive in the next hour from {station}")
        for element in json_obj['payload']['arrivals']:
            type_train = element['product']['longCategoryName']
            origin = element['origin']
            track = element['plannedTrack']
            time = element['plannedDateTime'][11:16]
            print(f'The {type_train} from {origin} arrives at track'
            f' {track} at {time}')

        conn.close()
    except:
        print("Something went wrong...")
        return 1

    return 0 