import os
import sys
import mail

TAG = sys.argv[1]
EMAILS = sys.argv[2:]

# equivalent to: from parsers import TAG.lower(); parser = TAG.lower().Parser()
parser = getattr(__import__('parsers', globals(), locals(), [TAG.lower()], 0), TAG.lower()).Parser()
parser.parse()

# check if this item was alread processed
tmp_file = '/tmp/{tag}'.format(tag=TAG)
if os.path.exists(tmp_file):
  with open(tmp_file, 'r') as file:
    stored_id = file.readline().strip()
    if stored_id == str(parser.getId()):
      sys.exit(0)

with open(tmp_file, 'w') as file:
  file.write(str(parser.getId()))

mail_variables = parser.getVariables()

# File with raw css&html content of mail
mail_content = mail.format(**mail_variables)                   # "/tmp/<random_name>"

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
