import requests as req;
from bs4 import BeautifulSoup;
URL = "https://www.evo.com/shop/sale/ski/skis/ability_advanced-expert"
def scrape_evo():
    product_from_evo = [] #Brand,Title,img_src,price,compare_at,link
    entire_page = req.get(URL)
    soup = BeautifulSoup(entire_page.content,"html.parser")
    all_products = soup.find_all("div",{"class":"product-thumb-details"})
    for i,product in enumerate(all_products):
        temp = []
        #if i == 0 :
            #print(product.prettify())

        if i < 20 :
            titleString = product.find("span",{"class":"product-thumb-title"}).getText().split()
            brand = titleString [0]
            title = ' '.join(titleString[1:])
            img = product.find("img")["src"]
            price = product.find_all("span",{"class":"product-thumb-price"})[1].getText().split()[1]
            compare_at = product.find("span",{"class":"product-thumb-price"}).getText() 
            link = product.find("a")["href"]
            link = "https://www.evo.com"+link
        
            print("---------------") 
            print(brand)
            print(title)
            print(img)
            print(price)
            print(compare_at)
            print(link)
            temp.append(brand)
            temp.append(title)
            temp.append(img)
            temp.append(price)
            temp.append(compare_at)
            temp.append(link)
            product_from_evo.append(temp)
    return product_from_evo           


scrape_evo()