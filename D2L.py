#quick python script that takes domain names translates them to IP addresses and then extract important information!
import requests

while True:
    try:
        domain = input(">_Enter Domain Here: ")
        domain_to_ip = "http://ip-api.com/json/" + domain
        
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


        print('IP: ' + str(ip))
        print('Organization: ' + str(org))
        print('Country: ' + str(country))
        print('-----------------------------------------')
    except Exception as e:
        print("[?]\tpython error",e)

