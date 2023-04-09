# !pip install imgurpython
# !pip install imgurpython
# !pip install google-search-results

from imgurpython import ImgurClient
from serpapi import GoogleSearch
from pprint import pprint

# client_id = '76cc9b033545178'
# client_secret = '96afcd0976e8367173f6e738f1cf9ea3f3787263'

# client = ImgurClient(client_id, client_secret)


class UploadImage():
  def __init__(self):
    self.client_id = '76cc9b033545178'
    self.client_secret = '96afcd0976e8367173f6e738f1cf9ea3f3787263'
    self.client = ImgurClient(self.client_id, self.client_secret)
  
  def upload(self, image_path: str):
    data = self.client.upload_from_path(image_path)
    link = data['link']
    return link


# from pprint import pprint
class SearchImage():
  def __init__(self):
    self.params = {
        "engine": "google_reverse_image",
        "google_domain": "google.com",
        "image_url": "url",
        "api_key": "f1c8dbfae33655ed3a18405ed3cf53460d7f1725f6d042cb3d17c41e9726d812"
    }
    self.client = GoogleSearch(self.params)

  def search(self, image_url: str):
    self.client.params_dict['image_url'] = image_url
    data = self.client.get_dict()
    # pprint(data)
    return data






# # import pysftp as sftp
# import urllib.request as urllib2
# from urllib.request import urlopen
# from http.cookiejar import CookieJar
# import time
# import re
# cj = CookieJar()
# opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
# opener.addheaders =  [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

# def imageLookup():
#   # s = sftp.Connection(host="pythonprogramming.net")
#   # numToAdd = str(int(time.time()))
#   # # remotepath = 
#   # s.put()
#   # imagepath = 'image.png'
#   imagepath = 'http://i.gyazo.com/82ed00642007a857db454cfd19034cae.png'
#   x = 'http://google.com/searchbyimage?image url=http://i.gyazo.com/82ed00642007a857db454cfd19034cae.png'
#   googlepath = 'http://google.com/searchbyimage?image_url='+imagepath
#   sourceCode = opener.open(googlepath)
#   # print(sourceCode)
#   findLinks = re.findall(r'<div class="rg_meta">{"os":".*?","cb":.*?,"ou":"(.*?)","rh":"',sourceCode)
#   print(findLinks)
#   # for eachThing in findLinks:
#   #     print(eachThing)
# imageLookup()
