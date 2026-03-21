import requests
import time

Ipinfochave="572e41b0d1c322"

def buscar_ip(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json?token={Ipinfochave}")
    return response.json()