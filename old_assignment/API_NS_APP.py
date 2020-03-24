"""
Reisinformatie API
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64

key1 = '1f11dc707bbd450cbcd02d643dfd4ec4'
key2 = '07975501f3ff42a5945acdd2193d0cfa'

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': key1,
}
"""
params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/reisinformatie-api/api/v2/stations?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))

"""

"""
Get departures from the Reisinformatie API
"""

params = urllib.parse.urlencode({
    # Request parameters
    'dateTime': '2020-03-18T18:20:50.52Z',
    'maxJourneys': '25',
    'lang': 'nl',
    'station': 'Hr',
})

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/reisinformatie-api/api/v2/departures?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))
