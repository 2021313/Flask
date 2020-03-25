import pytest
from Scraper import PageScraper

def test_PageScraper_List():
    containsTitle = False
    containsPrice = False
    consolelist, a, b = PageScraper()
    print(a, b)
    print(len(consolelist))
    i = 0
    for i in range(len(consolelist)):
        try:
            print(consolelist[i])
            if (len(consolelist[i]['title']) > 0):
                containsTitle = True
            if (consolelist[i]['price'] > 0):
                containsPrice = True
                break
        except:
            print("Fail")
            i + 1
    assert containsTitle == True and containsPrice == True

def test_PageScraper_Min_Max():
    z, maxprice, minprice = PageScraper()
    print(z[0])
    assert minprice > 0 and maxprice > 0