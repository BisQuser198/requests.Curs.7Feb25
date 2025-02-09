# AI boom right now - easy to get hired; internship ; framework to generate code: react native & then convert into other type of code
# difference mobile web - distance (ex: bluetooth) -- is the mobile app really necessary
# 3x categ site: prezentare, online stores, aplicatii web



# import requests
# url = 'https://www.link-academy.com'
# response = requests.get(url)
# print(response)
# print(response.status_code)
# print(type(response.content))
#print(response.text)

# file_handler = open("link-academy2.html", "w", encoding="utf-8")
# file_handler.write(response.text)
# file_handler.close()

# with open ("link-academy.html", "w", encoding="utf-8") as file_handler:
#     file_handler.write(response.text)

#-----------------------

# import requests
# import random
# import json
# import time

# api_options = ["", "-gcp", "1", "2", "3", "4"]
# valoare = random.choice(api_options)
# BASE_URL = f"https://api{valoare}.binance.com"
# print(BASE_URL)

# PATH = "/api/v3/avgPrice"

# URL = BASE_URL + PATH
# print(URL)

# symbol = "ETHBTC"

# def call_api():
#     response = requests.get(URL, params={'symbol':symbol})
#     print(response.content)

#     # deserialize
#     json_response = json.loads(response.content) # load vs loads - read from file fpu vs read from memory 
#     print(json_response, type(json_response)) # OUT: type dict
#     price = json_response['price']
#     print("price = ", price)

#     with open("ethereum.txt", "a") as fwriter:
#         fwriter.write(price)
#         fwriter.write("\n")
# # json.dumps
#     # json_dumps = json.dumps(response.content)
#     # print(json_dumps)

# if __name__ == "__main__":
#     while True:
#         call_api()
#         doarme =random.randint(1,3)
#         time.sleep(doarme)


# #-----------------------
# with open("ethereum.txt", "r") as file_reader:
#     continut = file_reader.read()
#     linii = continut.strip().split("\n") # strip to remove the spaces
#     linii = [float(i) for i in linii] ; print(linii) # convert to float
#     media = sum(linii) / len(linii)
#     print("media = ", media)

# ---------------

import requests
import json
from pprint import pprint

latitudine = 44.432384
longitudine = 26.1063209

BASE_URL = "https://api.open-meteo.com"
PATH = "/v1/forecast"
URL = BASE_URL + PATH

parametri = {'latitude': latitudine, 'longitude': longitudine, 'current':'temperature_2m'}

response = requests.get(URL, params=parametri)
print(response.request.url)
print(response.status_code)
print(response.content)

#$ curl "https://api.open-meteo.com/v1/forecast?latitude=52.52&longitude=13.41&hourly=temperature_2m"

json_response = json.loads(response.content) # convert to dictionary
print('temperature este:', json_response['current']['temperature_2m'])


#     json_response = json.loads(response.content) # load vs loads - read from file fpu vs read from memory 
#     print(json_response, type(json_response)) # OUT: type dict
#     price = json_response['price']
#     print("price = ", price)



# json.dumps # serialize

# URL STRUCTURE IS UP TO ? - which is followed by parameters

# NA: review the presentation
# what are you doing wrong incorrectly with the github
# install pypi.org requests ; pip install requests
# https://github.com/binance/binance-spot-api-docs/blob/master/rest-api.md#general-api-information
# json language is intermediary language (interconvertible)