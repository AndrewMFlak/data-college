import time
import datetime
from bs4 import BeautifulSoup
import urllib.request,urllib.parse
import pymongo
try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
except pymongo.errors.ConnectionFailure as e:
    print(e)


import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl._create_unverified_context



url = 'https://collegescorecard.ed.gov/data/'
