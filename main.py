import requests
from datetime import datetime
from datetime import timedelta

USERNAME = "jocarbon"
TOKEN = "greja90ao"

pixela_endpoint = "https://pixe.la/v1/users"
user_params = {
  # token similar to api key
  "token": "greja90ao",
  "username": "jocarbon",
  "agreeTermsOfService": "yes",
  "notMinor": "yes"
}

####### POST: create a user account

# # arguments include api end point
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

######## dont need the above anymore because I created my user


######## POST: create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
  "id": "runner3000",
  "name": "run tracker",
  "unit": "miles",
  "type": "float",
  "color": "sora"
}

headers = {
  "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# find at : https://pixe.la/v1/users/jocarbon/graphs/runner3000.html
######## again no longer need above because graph is already created


######### POST: post value to graph
today = datetime.now()
yesterday = today - timedelta(days = 1)
# print(today.strftime("%Y%m%d"))

pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_params['id']}"

pixel_params = {
  "date": yesterday.strftime("%Y%m%d"),
  "quantity": "4.1",
}

# pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(pixel_response.text)

######### PUT: update a pixel
update_endpoint = f"{pixel_endpoint}/{yesterday.strftime('%Y%m%d')}"

update_params = {
  "quantity": "5.85"
}

# update_response = requests.put(url=update_endpoint, json=update_params, headers=headers)
# print(update_response.text)

######### DELETE: delete a pixel
delete_response = requests.delete(url=update_endpoint, headers=headers)
print(delete_response.text)
