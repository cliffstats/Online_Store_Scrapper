####WEBSCRAPPING KILIMALL USING BS4 IN PYTHON
from urllib.request import urlopen as uReq
from nltk import text
from bs4 import BeautifulSoup as soup

kilimall_url = "https://www.kilimall.co.ke/promotion.html"
kilimall_url

papito = uReq(kilimall_url)
kilimall_html = papito.read()
papito.close()

page_soup = soup(kilimall_html, "html.parser")

holders = page_soup.findAll("li",{"class" : "item"})
len(holders)

filename = "kilimalldeals.csv"
fif = open (filename, "w")
headers = " Product_Name , Prices \n"
fif.write(headers)

for holder in holders:
    name_holder = name_holder = holder.findAll("h2", {"class":"goods-name"})
    productName = name_holder[0].text
    price_holder = holder.findAll("div", {"class":"goods-price"})
    offerPrice = price_holder[0].text
    offerPrice = offerPrice.replace("\n", "|")
    fif.write( productName.replace("," , "|") + "," + offerPrice.replace("," , "-") + "\n")
fif.close()

#for holder in holders:
#    name_holder = name_holder = holder.findAll("h2", {"class":"goods-name"})
#    productName = name_holder[0].text
#    highprice_holder = holder.findAll("div", {"class":"goods-price"})
#    marketPrice = highprice_holder[0].text
#    lowprice_holder = holder.findAll("em", {"class":"sale-price"})
#    offerPrice = lowprice_holder[0].text
#    f.write(productName.replace("," , "|") + "," + marketPrice + "," + offerPrice + "\n")
#f.close()