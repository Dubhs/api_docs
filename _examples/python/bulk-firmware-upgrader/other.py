import http.client
import json

def auth():
    conn = http.client.HTTPConnection("192.168.1.1")
    payload = json.dumps({
      "username": "root",
      "password": "admin"
    })
    headers = {
      'Content-Type': 'application/json',
      'Accept': 'application/json'
    }
    conn.request("POST", "/cgi.lua/apiv1/login", payload, headers)
    res = conn.getresponse()
    data = res.read()
    json_data = json.loads(data)
    api_key = json_data["token"]
    return api_key

