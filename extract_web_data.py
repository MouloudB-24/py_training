import requests

url = "https://openclassrooms.com/fr/"

page = requests.get(url)

print(page.content)