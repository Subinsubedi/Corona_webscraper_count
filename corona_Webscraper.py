

import requests
from bs4 import BeautifulSoup
URL = "https://www.worldometers.info/coronavirus/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')



results = soup.find_all(id='maincounter-wrap')

print(results[0].text)
print(results[1].text)
print(results[2].text)


#print(results.prettify())
