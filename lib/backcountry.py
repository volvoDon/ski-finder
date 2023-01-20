import requests as req;
from bs4 import BeautifulSoup;
URL = "https://www.backcountry.com/alpine-skiing?p=group_id%3Abc-alpine-skis&sort=-discountpercent"
def scrape_backcountry():
    skis_from_bc = [] #Brand,Title,img_src,price,compare_at,percent_off,link
    entire_page = req.get(URL)
    soup = BeautifulSoup(entire_page.content,"html.parser")
    all_skis = soup.find_all("div",{"data-id":"productListingItems"})
    for i,ski in enumerate(all_skis):
        temp = []
        if i == 0:
            print(ski.prettify())
        if ski.find("div",{"data-id":"productSalesPrice"}) is not None:
            brand = ski.find("p",{"data-id":"productListingBrand"}).getText()
            title = ski.find("h2",{"data-id":"productListingTitle"}).getText()
            price = ski.find("span",{"data-id":"productListingPrice"}).getText().split()
            link = ski.find("a")["href"]
            compare_at = price[-1]
            price = price[2]
            img_src = ski.find("img")["src"]
            img_src = "http:"+img_src
            link = "https://www.backcountry.com"+link
            temp.append(brand)
            temp.append(title)
            temp.append(img_src)
            temp.append(price)
            temp.append(compare_at)
            temp.append(link)
            skis_from_bc.append(temp)
            print("Brand: ",brand)
            print("title: ",title)
            print("img_src: ",img_src)
            print("price: ",price)
            print("compare_at: ",compare_at)
            print("link: ",link)
            print("------------")
            
    return skis_from_bc



