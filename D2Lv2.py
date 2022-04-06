import argparse, pathlib
import requests

parser = argparse.ArgumentParser()
parser.add_argument('file', type=pathlib.Path)
args = parser.parse_args()

with args.file.open('r') as file:
    book = [line.rstrip('\n') for line in file]

for address in book:
    domain_to_ip = "http://ip-api.com/json/" + address
        
    d_r = requests.get(domain_to_ip)
    d_response = d_r.json()
    query = d_response["query"]
    convert_ip = query

    URL = "https://api.iplocation.net/?cmd=ip-country&ip=" + query
    r = requests.get(URL)
    response = r.json()

    org =response["isp"]
    country = response["country_name"]
    ip = response["ip"]

    print('Domain: ' + address)
    print('IP: ' + str(ip))
    print('Organization: ' + str(org))
    print('Country: ' + str(country))
    print('-----------------------------------------')
