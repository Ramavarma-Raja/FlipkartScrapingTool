import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

Product_names = []
Discounted_price = []
Original_price = []
Discount_percentage = []
Product_desc = []
Product_rating = []

page = 1
pages = 10
page_flag = True

text = input("Search box : ")
querry = text.replace(" ", "+")

print(f"Scraping data for {text}")

while page <= pages:
    
    url = "https://www.flipkart.com/search?q="+querry+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(page)
    response = requests.get(url)
    if response.status_code != 200:
        print("URL NOT AVAILABLE!")
        quit()
    soup = BeautifulSoup(response.text, "html.parser")
    
    page += 1
    
    #to get the total number of pages for the querry

    if page_flag is True:
        page_data = soup.find("div", class_="_1G0WLw")
        data_text = []
        for item in page_data:
                data_text.append(item.text)
        text = data_text[0]
        parts = text.split()
        pages = int(parts[-1])
        page_flag = False

    
    #to find product information

    box = soup.find("div", class_="DOjaWF gdgoEp")

    try:
        products = box.find_all("div", class_="KzDlHZ")
        for product in products:
            Product_names.append(product.text)
        
        products = box.find_all("div", class_="col col-5-12 BfVC2z")
        for product in products:
            item = product.find("div", class_="Nx9bqj _4b5DiR")
            if item:
                price = re.sub(r"[\u20B9]", "", item.text)
                Discounted_price.append(price)
            else:
                Discounted_price.append("N/A")
        
        for product in products:
            item = product.find("div", class_="yRaY8j ZYYwLA")
            if item:
                price = re.sub(r"[\u20B9]", "", item.text)
                Original_price.append(price)
            else:
                Original_price.append("N/A")

        for product in products:
            item = product.find("div", class_="UkUFwK")
            if item:
                Discount_percentage.append(item.text)
            else:
                Discount_percentage.append("N/A")
        
        products = box.find_all("div", class_="_6NESgJ")
        for product in products:
             Product_desc.append(product.text)
        
        # products = box.find_all("span", class_="_5OesEi")
        # for product in products:
        #      Product_rating.append(product.text)
  
    except Exception:
        pass

print(f"{len(Product_names)} items found!")

#making a data frame

try:
     
    df = pd.DataFrame({
        "Sl. No." : range(1,len(Product_names)+1),
        "Product Name" : Product_names,
        "Discounted Price" : Discounted_price,
        "Original Price" : Original_price,
        "Discount %" : Discount_percentage,
        "Product Description" : Product_desc,
        # "Product Rating" : Product_rating
    })

    
    #converting to a csv file

    text = input("Save the CSV file as : ")

    if ".csv" not in text:
        file_name = text + ".csv"
    else:
        file_name = text

    df.to_csv(file_name, index=False)

    print("File Created!")

except Exception:
     print("File not created!")
