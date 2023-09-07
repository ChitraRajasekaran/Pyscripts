import requests
from PIL import Image
import urllib
#FINAL SOLUTION - Beautifulsoup : build a web scraper to download images from a website!

import requests
from PIL import Image
import urllib
from bs4 import BeautifulSoup
import requests

URL = "https://"
image_name = "image"

page = requests.get(URL)

# print(page.text)

soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(class_="carousel-wrapper1")
images = results.find_all("img", class_="rimage__image")
for idx, image in enumerate(images):
    source = image.get("src")
    if source:
        print(source, end="\n"*2)
        img = Image.open(requests.get("https:"+source, stream = True).raw)
        img.save(str(idx)+image_name+'.jpg')

# img_url = 'https://'
# response = requests.get(img_url)
# # print(response)
# if response.status_code:
#     fp = open('2_img .png', 'wb')
#     fp.write(response.content)
#     fp.close()


# import urllib.request
# contents = urllib.request.urlopen("https://").read()
# print(contents)

# import requests
# from bs4 import BeautifulSoup as bs


# r = requests.get('https://')

# soup = bs(r.content)
# # print(soup.prettify())

# images = soup.select('div img')
# images_url = images[0]['src']


# img_data = requests.get(images_url).content 

# with open('c.jpg', 'wb') as handler: 

#        handler.write(img_data) 
