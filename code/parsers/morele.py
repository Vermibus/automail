from bs4 import BeautifulSoup
import certifi
import urllib3
import re

from parsers import parser

class Parser(parser.ParserAbstractClass):

  def __init__(self):
    self.url = 'https://www.morele.net/'

  def __str__(self):
    return 'morele.pl_parser'

  def parse(self):
    https = urllib3.PoolManager(
      cert_reqs='CERT_REQUIRED',
      ca_certs=certifi.where(),
    )
    response = https.request('GET', self.url)
    soup = BeautifulSoup(response.data, 'html.parser')
    
    #item_name
    self.item_name = soup.find('div', class_='promo-box-name').find('a').string.strip()

    #old_price, new_price
    self.old_price = float( re.search('(\d+\.*\d*)', soup.find('div', class_='promo-box-old-price').string).groups(0)[0])
    self.new_price = float( re.search('(\d+\.*\d*)', soup.find('div', class_='promo-box-new-price').string).groups(0)[0])

    #item_link
    self.item_link = soup.find('div', class_='promo-box-name').find('a')['href']

    #item_specification & item_image
    item_response = https.request('GET', self.item_link)
    item_soup = BeautifulSoup(item_response.data, 'html.parser')

    self.item_image = item_soup.find('img', class_='lazy')
    self.item_image['src'] = self.item_image['data-cfsrc']
    for attr in ['height', 'width', 'style', 'data-cfsrc']:
      del self.item_image[attr]

    tmp_item_specification = item_soup.find('div', class_='specification-table')
    self.item_specification  = ''

    for tag in tmp_item_specification.find_all(['div', *['h'+ str(x) for x in range(1,8)]], recursive=False):
      if tag.name == 'div':
        # table with specification group
        self.item_specification  += '<table>'
        for row in tag.find_all('div', class_='table-info-item', recursive=False):
          name = row.find('div', class_='name').get_text(strip=True)
          value = row.find('div', class_='info-item').get_text(strip=True)
          self.item_specification  += '<tr><td>{name}</td><td>{value}</td></tr>'.format(name=name, value=value)
        self.item_specification  += '</table>'
      else:
        # header
        self.item_specification  += str(tag)
