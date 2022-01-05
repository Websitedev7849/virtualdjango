import requests
import json
import os
from bs4 import BeautifulSoup
from dotenv import load_dotenv

load_dotenv()


"""
{ 
    "asin": "B08L5VPTDK",
    "name": "New Apple iPhone 12 Pro (256GB) - Gold",
    "price": "99,900.00"
    "url": "https://www.amazon.in/New-Apple-iPhone-Pro-256GB/dp/B08L5VPTDK?ref_=Oct_DLandingS_D_9085df6d_60&smid=A14CZOWI0VEHLG"
    "date": "YYYY-MM-DD"
}
"""

class Product:

    def __init__(self, url):
        self.url = url
        self.raw_data = self.getRawData()
        self.asin = self.get_asin()
        self.name = self.getName()
        self.price = self.getPrice()
        # self.date = datetime.datetime.year + datetime.datetime.month + datetime.datetime.date

    def getRawData(self):
        url = "https://api.rainforestapi.com/request?api_key=" + os.getenv("RAINFOREST_API_KEY") +"&type=product&url=" + self.url
        # print(requests.get(url).text)
        return json.loads(requests.get(url).text)

    def getName(self):
        return self.raw_data["product"]["title"]
    
    def get_asin(self):
        return self.raw_data["product"]["asin"]

    def getPrice(self):
        URL = self.url

        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

        page = requests.get( URL, headers=headers)

        soup = BeautifulSoup(page.content, "html.parser")

        price = soup.find("span", {"class": "a-offscreen"})

        priceToReturn = price.text[1:].replace(",", "")

        return float(priceToReturn)

    def toString(self):
        return  "{" + f' "asin": "{self.asin}", "name": "{self.name}", "price" : {self.price}, "url" : "{self.url}" ' + "}"

