import requests
from datetime import datetime, timedelta

USERNAME = "aaronlee"
TOKEN = "8932u95mflemfopwefw"
GRAPHID = "graph001"

pixela_url = "https://pixe.la/v1/users"

user_config = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_url, json=user_config)
# print(response.text)

graph_url = f"{pixela_url}/{USERNAME}/graphs"

graph_config = {
    "id": "graph001",
    "name": "Coding Graph",
    "unit": "Hour",
    "type": "float",
    "color": "ajisai"
}

graph_header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_url, json=graph_config, headers=graph_header)
# print(response.text)

today = datetime.now()
# today = datetime(year=2022, month=8, day=1)
# formatted_today = datetime.strftime(today, "%Y%m%d")
today_date = today.strftime("%Y%m%d")

post_graph_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPHID}"

post_graph_config = {
    "date": today_date,
    "quantity": "3"
}

# response = requests.post(url=post_graph_url, json=post_graph_config, headers=graph_header)
# print(response.text)


update_graph_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPHID}/{today_date}"

update_graph_config = {
    "quantity": "3"
}

# response = requests.put(url=update_graph_url, json=update_graph_config, headers=graph_header)
# print(response.text)

yesterday = today - timedelta(1)
yesterday_date = yesterday.strftime("%Y%m%d")

delete_pixel_url = f"{pixela_url}/{USERNAME}/graphs/{GRAPHID}/{yesterday_date}"

# response = requests.delete(url=delete_pixel_url, headers=graph_header)
# print(response.text)