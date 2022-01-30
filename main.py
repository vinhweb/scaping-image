import requests
import pandas as pd
from bs4 import BeautifulSoup

pageTarget = 'https://kenh14.vn/'
page = requests.get(pageTarget)
soup = BeautifulSoup(page.content, 'html.parser')
wrapper = soup.find('body')

images = wrapper.find_all("img")
for image in images:
  imgData = image['src']
  print(imgData)
  if("data:image" not in imgData):
    if(imgData):
      downloadPath = './download'
      filename = imgData.split('/')[-1]

      response = requests.get(imgData)

      file = open(downloadPath + filename, "wb")
      file.write(response.content)
      file.close()
