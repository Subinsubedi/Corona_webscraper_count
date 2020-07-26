
'''
import requests
from bs4 import BeautifulSoup

jblCharge4URL = 'https://www.amazon.de/JBL-Charge-Bluetooth-Lautsprecher-Schwarz-      integrierter/dp/B07HGHRYCY/ref=sr_1_2_sspa?__mk_de_DE=%C3%85M%C3%85%C5%BD%C3%95%C3%91&  keywords=jbl+charge+4&qid=1562775856&s=gateway&sr=8-2-spons&psc=1'

def get_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')
    return soup

def get_product_name(url):
    soup = get_page(url)
    try:
        title = soup.find(id="productTitle")
        print("SUCCESS")

    except AttributeError:
        print("ERROR")
    return(title)
       
print(get_product_name(jblCharge4URL))
'''
import requests
from bs4 import BeautifulSoup
URL = "https://www.worldometers.info/coronavirus/"

page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')



results = soup.find_all(id='maincounter-wrap')

print(results[0].text)
print(results[1].text)
print(results[2].text)


#hmm
#print(results.prettify())
