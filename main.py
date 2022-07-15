
import requests
from datetime import datetime

USERNAME = "chetan2002"
TOKEN = "***********"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token":TOKEN,
    "username":USERNAME,
    "agreeTermsOfService":"yes",
    "notMinor":"yes"
}


graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id":GRAPH_ID,
    "name":"Protein Intake",
    "unit":"grams",
    "type":"float",
    "color":"momiji"
}

headers = {
    "X-USER-TOKEN":TOKEN
}


pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

intake = input("How much protein did you intake today?")

pixel_data = {
    "date":today.strftime("%Y%m%d"),
    "quantity":intake
}

response = requests.post(url=pixel_creation_endpoint,json=pixel_data,headers=headers)
print(response.text)

#update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

#ew_pixel_data = {
#    "quantity":"127.33"
#}

#response = requests.put(url=update_endpoint,json=new_pixel_data,headers=headers)