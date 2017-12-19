from bs4 import BeautifulSoup as beautifulsoup
import tempfile
import certifi
import urllib3
import re
import os 
import sys

tag = sys.argv[1]
url = sys.argv[2]
emails = sys.argv[3:]

### Regex for hotShot link. 
link_regex = 'window\.location\s=\s"(\/goracy_strzal\/\d+)";'

### Connecting by https to main page and preparsing the content with beautifulsoup4

https = urllib3.PoolManager(
		cert_reqs='CERT_REQUIRED',
		ca_certs=certifi.where(),
	)

response = https.request('GET', url)
soup = beautifulsoup(response.data, 'html.parser')

### Getting the content about hotShot from main page

item_name = soup.find('p', class_='product-name').string
old_price = float( re.search('(\d+\.*\d*)', soup.find('div', class_='old-price').string.replace(' ','').replace(',','.') ).groups(0)[0] )
new_price = float( re.search('(\d+\.*\d*)', soup.find('div', class_='new-price').string.replace(' ','').replace(',','.') ).groups(0)[0] )

# Get the /hotShot/itemID from JS script. 
item_hotshot = re.search(link_regex, soup.find('div', id='hotShot').parent.find('script').string).groups(0)[0][1:]

# item_link is the full link of HotShot
item_link = url + item_hotshot
item_response = https.request('GET', item_link)
item_soup = beautifulsoup(item_response.data, 'html.parser')

### Drawing the image of hotShot, and removing the </p> tag with its content
item_image = soup.find('div', id='hotShot').find('img', class_='img-responsive')
[ s.extract() for s in item_image('p') ]
item_image['href'] = item_link

item_specification = str( item_soup.find('span', id='specification').parent.parent.parent.find('tbody')
					).replace('tbody','table').replace('<table>','<table class="specification">')

### Generating the structure of mail.

mail_content = tempfile.NamedTemporaryFile(mode='w')

mail_header = """
<html> 
<head>
	<style type="text/css">

  table.information td { 
    font-family: "Open Sans", sans-serif;
    fint-size: 30px;
  }

  table.specification { 
    border-collapse: collapse;
    border-top-color: rgb(221, 221, 221);
    border-top-style: solid;
    border-top-width: 1px;
    box-sizing: border-box;
    color: rgb(77, 77, 77);
    display: table-cell;
    float: none;
    font-family: "Open Sans", sans-serif;
    text-align: left; 
    font-size: 14px;
    height: 36px;
    line-height: 20px;
    vertical-align: top;
  }

  table.specification td, table.specification th {
    border: 1px solid gray;
    background-color: white;
  }

  table.specification th { 
    padding-right: 5px;
  }

	</style>
</head>
"""

item_information = """
<h2>{name}</h2>
<table class='information'>
	<tr> <td><b>Cena</b></td> <td>: <s>{old}</s> {new}</td> </tr>
	<tr> <td><b>Onionmeter</b></td> <td>: -{onion}zł </td> </tr>
</table>
""".format(name=item_name, old=old_price, new=new_price, onion=old_price-new_price)

mail_content.write( mail_header )
mail_content.write( '<body>' )
mail_content.write(	item_information )
mail_content.write( str(item_image) )
mail_content.write( '<h2>Specyfikacja:</h2>' + item_specification )
mail_content.write( '</body></html>' )
mail_content.seek(0)


receivers = ' '.join([ '-b ' + email for email in emails ])
subject = "-s '" + tag + str(new_price) + 'zł - ' + item_name  + " ' "

### SEND IT !
command = "mutt -e 'set content_type=text/html' " + subject + receivers + ' < ' + mail_content.name
os.system(command)

