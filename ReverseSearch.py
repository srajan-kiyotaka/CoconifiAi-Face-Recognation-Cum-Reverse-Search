# import pysftp as sftp
import urllib.request as urllib2
from urllib.request import urlopen
from http.cookiejar import CookieJar
import time
import re
cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders =  [('User-agent', 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17')]

def imageLookup():
  # s = sftp.Connection(host="pythonprogramming.net")
  # numToAdd = str(int(time.time()))
  # # remotepath = 
  # s.put()
  # imagepath = 'image.png'
  imagepath = 'http://i.gyazo.com/82ed00642007a857db454cfd19034cae.png'
  x = 'http://google.com/searchbyimage?image url=http://i.gyazo.com/82ed00642007a857db454cfd19034cae.png'
  googlepath = 'http://google.com/searchbyimage?image_url='+imagepath
  sourceCode = opener.open(googlepath)
  # print(sourceCode)
  findLinks = re.findall(r'<div class="rg_meta">{"os":".*?","cb":.*?,"ou":"(.*?)","rh":"',sourceCode)
  print(findLinks)
  # for eachThing in findLinks:
  #     print(eachThing)
imageLookup()
