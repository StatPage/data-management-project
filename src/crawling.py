import requests
from bs4 import BeautifulSoup

def get_and_parse(url):
    req = requests.get(url)
    soup = BeautifulSoup(req.content, 'html.parser')
    return soup
