import requests

NETBOX_URL = "http://3.233.217.219:8000"
API_TOKEN = "14d4c6a69bf04de9ea52c1174455c765d47c9e5a"

headers = {
    "Authorization": f"Token {API_TOKEN}",
    "Content-Type": "application/json",
}

response = requests.get(
    f"{NETBOX_URL}/api/dcim/sites/",
    headers=headers
)

response.raise_for_status()

sites = response.json()["results"]

for site in sites:
    print(f"Site Name: {site['name']}, Slug: {site['slug']}")