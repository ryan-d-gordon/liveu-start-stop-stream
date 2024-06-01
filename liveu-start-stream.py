#! /usr/bin/python3
import requests

# WARNING! This script is for demonstration purposes only.
# It is bad security practice to store credentials in scripts directly.

# Replace 'YOUR_BASE64_LUCENTRAL_CREDS' with your LUCentral username:password encoded into base64.
lucentral_creds = 'YOUR_BASE64_LUCENTRAL_CREDS'

# Replace 'YOUR_LIVEU_UNIT_SERIAL_NUMBER' with the serial of the unit you want to start/stop.
liveu_unit_serial = 'YOUR_LIVEU_UNIT_SERIAL_NUMBER'


### AUTHORIZATION ###

# Form Authorization Request URL to reteive OAuth token
auth_url = "https://lu-central.liveu.tv:8543/luc/luc-oauth-server/auth-server/j_oauth_token_grant"

payload = ""

headers = {
    'Authorization': "Basic " + lucentral_creds,
    'cache-control': "no-cache"
}

json_data = requests.request("POST", auth_url, data=payload, headers=headers)

data = json_data.json()

if 'access_token' not in data:
    raise ValueError("Authorization failed, access token not found")

token = "Bearer " + data['access_token']



### LIVEU UNIT COMMAND OR ACTION ###

# Form Command/Action URL to control unit's stream
command_url = f"https://lu-central.liveu.tv:8543/luc/luc-core-web/rest/v0/units/{liveu_unit_serial}/stream"

headers = {
    'Authorization': token,
    'cache-control': "no-cache"
}

# POST commands will start a stream
resp = requests.post(command_url, headers=headers, data=payload)

print(resp.text)
