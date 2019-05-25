import time
import datetime
from bs4 import BeautifulSoup
import urllib.request,urllib.parse
#==================PyMongo===================>
import pymongo
try:
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
except pymongo.errors.ConnectionFailure as e:
    print(e)

#==============SSL Certificate==================>
import ssl
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl._create_unverified_context




mydb = myclient["dataSets"]
mycol = mydb["collegeData"]
mycol.create_index("_id")

url = 'https://collegescorecard.ed.gov/data/'

import zipfile
with zipfile.ZipFile(url,"r") as zipedi:
    zipedi.extractall("./")
