from PIL import Image
import requests
from io import BytesIO

url = "https://api.opensea.io/api/v1/asset/0xb47e3cd837ddf8e4c57f05d70ab865de6e193bbb/1/"

# ! SPOOFED USER-AGENT
usr = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:97.0) Gecko/20100101 Firefox/97.0"}



response = requests.request("GET", url, headers=usr)

print(response.status_code)


# display image 

imageUrl = response.json()["image_url"]
print(imageUrl)
response = requests.get(imageUrl)
if response.status_code == 200:
    with open("/tmp/tmp.png", 'wb') as f:
        f.write(response.content)
img = Image.open("/tmp/tmp.png")
img.show()

# print(response.text)