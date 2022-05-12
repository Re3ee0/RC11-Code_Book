import requests

url = "https://api.foursquare.com/v3/places/search?ll=48.894326%2C2.248671&radius=500&limit=20"

headers = {
    "Accept": "application/json",
    "Authorization": "fsq37t/Q9AvUtYvgDGQ7PnLy47ErlW3mYe6I4cGh3UHnZJ0="
}

response = requests.request("GET", url, headers=headers)

print(response.text)