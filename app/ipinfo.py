import requests

Ipinfochave="XXXXXXXXXXXXXXx"

def buscar_ip(ip):
    response = requests.get(f"https://ipinfo.io/{ip}/json?token={Ipinfochave}")
    return response.json()