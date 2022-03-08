from requests import get
import socket
import json
def getinfo () :
    ip = get('https://api.ipify.org?format=json').text
    hostname=socket.gethostname()
    x = json.loads(ip)
    x.update({"hostname":hostname})
    return (x)