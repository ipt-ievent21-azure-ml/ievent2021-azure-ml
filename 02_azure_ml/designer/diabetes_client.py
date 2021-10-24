#!/usr/bin/env python3

import urllib.request
import json
import os
import ssl


def allowSelfSignedHttps(allowed):
    # bypass the server certificate verification on client side
    if allowed and not os.environ.get('PYTHONHTTPSVERIFY', '') and getattr(ssl, '_create_unverified_context', None):
        ssl._create_default_https_context = ssl._create_unverified_context


# this line is needed if you use self-signed certificate in your scoring service.
allowSelfSignedHttps(True)

# Request data goes here
data = {
    "Inputs": {
        "WebServiceInput0":
        [
            {
                'AGE': "59",
                'SEX': "2",
                'BMI': "32.1",
                'BP': "101",
                'S1': "157",
                'S2': "93.2",
                'S3': "38",
                'S4': "4",
                'S5': "4.8598",
                'S6': "87",
            },
        ],
    },
    "GlobalParameters": {
    }
}

body = str.encode(json.dumps(data))

url = 'PASTE_YOUR_REST_ENDPOINT_HERE'
api_key = 'PASTE_YOUR_API_KEY_HERE'
headers = {'Content-Type': 'application/json',
           'Authorization': ('Bearer ' + api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))
