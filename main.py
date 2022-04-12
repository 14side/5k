import requests
from bs4 import BeautifulSoup
import json
import random
import re
from re import findall 

list = []
url = 'https://studynow.ru/dicta/allwords'

response = requests.get(url)

bs = BeautifulSoup(response.content, 'lxml')

words = bs.find_all('td')

for word in words:
    
    list.append(word.text)
list = str(list)
z = re.findall(r'[A-Za-z]+', list)
random.shuffle(z)

def save_data(title, data):
    with open(title, 'w', encoding = 'UTF-8') as f:
        json.dump(data, f, ensure_ascii = False, indent = 2)

save_data('5000_rand.json', z)
