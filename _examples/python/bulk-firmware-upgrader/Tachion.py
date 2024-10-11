import http.client
from operator import contains
import urllib.parse
import ssl
import os
import json

class Radio(http.client.HTTPConnection):
    def __init__(self, host, unsafe=False):
        if unsafe is True:
            #context=ssl._create_unverified_context()
            pass
        else:
            #context=None
            pass
            
        super().__init__(
            host=host, 
            #port=port,
            #context=context
            )
    
    def auth(self):
        payload = json.dumps({
            "username": "root",
            "password": "admin"
        })
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'Connection': 'keep-alive'
        }
        self.request("POST", "/cgi.lua/apiv1/login", payload, headers)
        res = self.getresponse()
        print(res.status)
        data = res.read()
        json_data = json.loads(data)
        print(data)
        api_key = json_data["token"]
        print("auth_suceed")
        print(json_data)
        return api_key
    
    def get_config(self, api_key):
        payload = ''
        headers = {
            'Accept': 'application/json',
            'Cookie': f"api_token={urllib.parse.quote(api_key)}"
        }
        print(headers)
        print(payload)
        self.request("GET", "/cgi.lua/apiv1/config", headers=headers)
        res = self.getresponse()
        print(res.status)
        data = res.read()
        print(data.decode("utf-8"))
    
    
    def post_config(self, api_key, config, dry_run):
        payload = json.dumps({
            "dry_run": dry_run, #boolean
            "config": json.loads(config)
        })
        print(urllib.parse.quote(api_key))
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json',
            'api_token': f'{api_key}'
        }
        print(headers)
        print(payload)
        print("here we go!")
        self.request("POST", "/cgi.lua/apiv1/config", payload, headers)
        res = self.getresponse()
        data = res.read()
        print(data.decode("utf-8"))