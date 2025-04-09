import requests
import datetime 

USERNAME = "asmsafisadi"
TOKEN = "Pumajuta?12"

pixela_endpoint = "https://pixe.la"
graph_pixel_endpoint = f"https://pixe.la/v1/users/{USERNAME}/graphs/graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# pixela_response = requests.post(url=pixela_endpoint, json=user_params)
# pixela_response.raise_for_status()
# print(pixela_response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph2",
    "name": "Reading Graph",
    "unit": "page",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN":TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

now = datetime.datetime.now()
a = (str(datetime.datetime.today()).split()[0].split("-"))
s = "".join(a)
s = str(int(s)-1)
print(s)

date = int(now.strftime("%Y%m%d"))-2
x = 5.5
pixel_config = {
    "date": str(date),
    "quantity": str(x+5),
}
# response = requests.post(url=graph_pixel_endpoint, headers=headers,json=pixel_config)
# response.raise_for_status()
# print(response.text)
update_pixel_endpoint = f"{pixela_endpoint}/v1/users/{USERNAME}/graphs/graph1/{date}"


update = {
    "quantity": "10.2",
    
}

response = requests.delete(url=update_pixel_endpoint, headers=headers)
print(response.text)


 