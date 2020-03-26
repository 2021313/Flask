#Scraper
import requests
from bs4 import BeautifulSoup

def PageScraper():
    cnt = 1
    page = 1 
    results = []
    minprice = None
    maxprice = None
    while cnt > 0:
        response = requests.get("https://www.trademe.co.nz/gaming/playstation-4/consoles?buy=buynow&page=" + str(page))
        soup = BeautifulSoup(response.text,"html.parser")
        itemlist = soup.findAll("div", {"class":"supergrid-listing"})
        cnt = len(itemlist)
        for item in itemlist:
            try:
                item_title = item.find("div", {"class":"title"}).text.strip()
                item_price = item.find("div", {"class":"listingBuyNowPrice"}).text.strip()
                item_price = float(item_price.strip("$"))
                results.append({"title":item_title,"price":item_price})
                if minprice == None or item_price < minprice:
                    minprice = item_price
                if maxprice == None or item_price > maxprice:
                    maxprice = item_price
            except:
                print("Something went wrong!")
        page = page + 1
    return results, maxprice, minprice