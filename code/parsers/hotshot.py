from bs4 import BeautifulSoup
import certifi
import urllib3
import re

from parsers import parser

class Parser(parser.ParserAbstractClass):

  def __init__(self):
    self.url = 'https://www.x-kom.pl/'

  def __str__(self):
    return 'x-kom.pl_parser'

  def parse(self):
    https = urllib3.PoolManager(
      cert_reqs='CERT_REQUIRED',
      ca_certs=certifi.where(),
    )
    response = https.request('GET', self.url)
    soup = BeautifulSoup(response.data, 'html.parser')
    
    #item_name
    self.item_name = soup.find('p', class_='product-name').string
    
    #old_price, new_price
    floating = lambda x: float( re.search('([ 0-9]+,\d+)', x).group(1).replace(',','.').replace(' ','') )
    self.old_price = floating( soup.find('div', class_='old-price').string )
    self.new_price = floating( soup.find('div', class_='new-price').string )
    
    #item_link
    item_script = soup.find('div', id='hotShot').parent.find('script').string
    self.item_link = self.url + re.search('(goracy_strzal/\d+)', item_script).group(1)
    
    #item_specification & item_image
    item_response = https.request('GET', self.item_link)
    item_soup = BeautifulSoup(item_response.data, 'html.parser')
    
    self.item_image = item_soup.find('a', class_="prettyphoto-fullscreen-item").find('img')
    self.item_specification = item_soup.find_all('table')[1]
