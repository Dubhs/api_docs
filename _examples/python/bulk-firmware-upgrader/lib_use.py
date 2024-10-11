import http.client
import urllib.parse
from Tachion import Radio as Tachion
import requests

radio = Tachion("192.168.77.15", unsafe=True)

#need to implement new connections. mayby use requests
api_key = radio.auth()
connection = http.client.HTTPConnection("192.168.77.15")
def get_config(connection, api_key):
        payload = ''
        headers = {
            'Accept': 'application/json',
            'Cookie': f"api_token={urllib.parse.quote(api_key)}"
        }
        print(headers)
        print(payload)
        connection.request("GET", "/cgi.lua/apiv1/config", headers=headers)
        res = connection.getresponse()
        print(res.status)
        data = res.read()
        print(data.decode("utf-8"))
get_config(connection, api_key)
#radio.post_config(api_key,'{"system":{"device_name":"Tachyon Networks PtMP","reset_button":{"enabled":true},"hostname":"tachyon-ptmp-ap","users":[{"username":"root","type":"admin","password_hash":"$1$6Hzch.yD$ULugJ982Yb1D0g8zhqv3T.","enabled":true},{"username":"guest","type":"read-only","password_hash":"$1$/DpVqAVi$ZwWGYO83CGVclJeuwBb5C0","enabled":true},{"username":"new","type":"admin","password_hash":"$1$mokR7kX6$CvqYTxcq450LVAUjRHVM51","enabled":true},{"username":"guest1","type":"read-only","password_hash":"$1$ohSsj1Ga$xF6ruORwRp1TNYmUjRgQn0","enabled":true}],"device_location":"A/V Closet","timezone":"America/Los_Angeles"},"wireless":{"radios":{"wlan0":{"channel_width":2160,"ssid":"tachyon-ptmp","channel":6,"max_mcs":12,"mode":"ap","passphrase":"passphrase","security":"wpapsk"}}},"network":{"wan":{"ipv6":{"enabled":false},"data_vlan":{"enabled":false},"ipv4":{"enabled":true,"prefix":24,"custom_dns":true,"dns_servers":["1.1.1.1","1.0.0.1"],"ipaddr":"192.168.1.1","dhcp_broadcast":false},"mgmt_vlan":{"enabled":false},"ip_mode":"dhcp"},"traffic_control":{"limit_download":{"enabled":false},"limit_upload":{"enabled":false}},"poe_out_enabled":false,"general":{"ageing_time":300,"mtu":1501}},"services":{"snmp":{"v2":{"enabled":true,"community":"public"},"v3":{"enabled":false}},"ping_watchdog":{"enabled":false},"http":{"https_port":443,"port":80},"remote_syslog":{"enabled":false},"snmp_traps":{"enabled":false},"discovery":{"enabled":true,"broadcast_protocols":{"lldp":true,"cdp":true,"mndp":true},"lldp_server":{"enabled":true}},"ntp":{"enabled":true,"servers":["time.google.com","time.cloudflare.com"]}}}', True)

'''
def make_request(method=None, url=None, headers=None, json=None):
    """
    Makes a REST API request using the provided HTTP/HTTPS method, URL, headers, JSON data.

    Args:
        method (str): The HTTP/HTTPS method to use for the request (e.g., "GET", "POST", "PUT", etc.).
        url (str): The URL to send the request to.
        headers (dict, optional): A dictionary of headers to include in the request.
        json (dict, optional): A dictionary of JSON data to include in the request body.

    Returns:
        The response object returned by the requests library.
    """

    # Send the request and get the response object
    response = requests.request(method=method, url=url, headers=headers, json=data)

    # Return the response object
    return response

ip = "192.168.77.15"
    
print(f"\nWill now attempt to upgrade device at {ip} ...")
cgi_url = f'http://{ip}/cgi.lua/apiv1/'

# Post login credentials to your device in order to authenticate using REST interface.
url = cgi_url + 'login'
data = {'username': "root", 'password': "admin"}
headers = {'accept': 'application/json', 'Content-Type': 'application/json'}
response = make_request(method='post', url=url, headers=headers, json=data)
# Check success of authentication.
if response.status_code == 200:
    print('Authentication successful!')
else:
    print(response.content)
    exit(1)
# Retrieve the authentication token.
auth_token = response.cookies.get_dict().get('token')
print(auth_token)
if not auth_token:
    print(response.content)
    exit(1)
    
    
url = cgi_url + 'config'
headers = {'accept': 'application/json', 'Cookie': f'api_token={auth_token}'}
print(headers)
response = make_request(method='get', url=url, headers=headers)
print(response.content)
'''