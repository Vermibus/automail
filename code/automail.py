import os
import sys 
import mail 

TAG = sys.argv[1]
#URL = sys.argv[2]
EMAILS = sys.argv[2:]

# equivalent to: from parsers import TAG.lower(); parser = TAG.lower().Parser() 
parser = getattr(__import__('parsers', globals(), locals(), [TAG.lower()], 0), TAG.lower()).Parser()
parser.parse()

mail_variables = parser.getVariables()

# File with raw css&html content of mail 
mail_content = mail.format(**mail_variables)                   # "/tmp/tmpasdf1234"

receivers = ' '.join( ['-b ' + email for email in EMAILS] )    # "-b e1@mail.com -b e2@gmail.com -b e3@mail.com"
subject = "-s '[{tag}] {new_price} zł - {item_name}'".format(  # "-s '[tag] 0zł - Any_item_name'"
  tag=TAG,
  new_price = mail_variables['new_price'],
  item_name = mail_variables['item_name'], 
)

command = "mutt -e 'set content_type=text/html' {subject} {receivers} < {mail_content}".format(
  subject = subject,
  receivers = receivers,
  mail_content = mail_content,
)
os.system(command)
