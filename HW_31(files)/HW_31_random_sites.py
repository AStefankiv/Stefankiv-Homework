import requests
import random

sites = ["google.com", "facebook.com", "twitter.com", "amazon.com", "apple.com"]
random_site = random.choice(sites)

url = f"https://{random_site}"

res = requests.get(url)

status_code = res.status_code
site_name = random_site.capitalize()
html_length = len(res.text)

print(f"Status Code: {status_code}")
print(f"Site Name: {site_name}")
print(f"HTML Length: {html_length}")