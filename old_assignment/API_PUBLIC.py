"""
Get all stations - public
"""

import http.client, urllib.request, urllib.parse, urllib.error, base64

key1 = '3196093573604900afc0f23c662f7b6c'
key2 = '0abe867efa804ddcb66cf98dc2426bf1'

headers = {
    # Request headers
    'Ocp-Apim-Subscription-Key': key1,
}

params = urllib.parse.urlencode({
})

try:
    conn = http.client.HTTPSConnection('gateway.apiportal.ns.nl')
    conn.request("GET", "/public-reisinformatie/api/v2/stations?%s" % params, "{body}", headers)
    response = conn.getresponse()
    data = response.read()
    print(data)
    conn.close()
except Exception as e:
    print("[Errno {0}] {1}".format(e.errno, e.strerror))