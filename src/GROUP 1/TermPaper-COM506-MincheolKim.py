# %%
# imoprting module for data crawling
import requests
from bs4 import BeautifulSoup

# Storing Danningn URL address in url variable.
url = "https://www.daangn.com/region/%EC%A0%9C%EC%A3%BC%ED%8A%B9%EB%B3%84%EC%9E%90%EC%B9%98%EB%8F%84"

# Save the response html in a variable called req
req=requests.get(url)

# Parse the html saved in req and store it in a variable called soup
soup=BeautifulSoup(req.content, 'html.parser')

# %%
soup.find('div',class_="card-photo")

# %%
# Item Name
item_name = soup.find_all('div',class_="card-desc")

# Region Name
region_name = soup.find_all('div',class_="card-region-name")

# Card Count
card_counts = soup.find_all("<span>")

#%%

card_counts

# %%
# 'Like' and 'Chat' have to be seperated.

print(card_counts)
# %%
