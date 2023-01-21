import requests as req;
from bs4 import BeautifulSoup;
URL = "https://www.evo.com/shop/sale/ski/skis/ability_advanced-expert"
def scrape_backcountry():
    product_from_evo = [] #Brand,Title,img_src,price,compare_at,link
    entire_page = req.get(URL)
    soup = BeautifulSoup(entire_page.content,"html.parser")
    all_products = soup.find_all("div",{"class":"product-thumb-details"})
    for i,product in enumerate(all_products):
        temp = []
        if i == 0 :
            titleString = product.find("span",{"class":"product-thumb-title"}).getText().split()
            brand = titleString [0]
            title = ' '.join(titleString[1:])
            img = product.find("img")["src"]
            price = product.find_all("span",{"class":"product-thumb-price"})[1].getText().split()[1]
            compare_at = product.find("span",{"class":"product-thumb-price"}).getText() 
            print(product.prettify())
            print("---------------") 
            print(brand)
            print(title)
            print(img)
            print(price)
            print(compare_at)


scrape_backcountry()