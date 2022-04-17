from PIL import Image
import requests
from bs4 import BeautifulSoup

# Vairables
urlPage = "https://miku-doujin.com/3n7oj/"
page = requests.get(urlPage)
soup = BeautifulSoup(page.text, 'html.parser')
findUrl = soup.find_all("img", {"class": ['lazy', 'lazy loaded']})
findTitle = soup.find_all('title')

# get the title
title = ""
for i in findTitle:
    title = i.get_text()

# get scr
images = [link.get('data-src') for link in findUrl]
# remove none from list
images = [url for url in images if url]

img = [
    Image.open(requests.get(urlImg, stream=True).raw)
    for urlImg in images
]

# convert jpg to pdf
img[0].save(
    title + '.pdf', "PDF", resolution=100.0, save_all=True, append_images=img[1:]
)
print('Finished 🥵')
