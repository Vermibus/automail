## Internal libs
import os

## External libs
import yaml

# Read and parse automail config
with open('/files/config.yml','rb') as file:
    config = yaml.load(file.read().decode('UTF-8'))

# Configure mutt to use specific GMAIL account
os.system('sed -ie "s/GMAIL_NAME/{GMAIL_NAME}/g" /var/spool/mail/.muttrc'.format(GMAIL_NAME=config['GMAIL_NAME']))
os.system('sed -ie "s/GMAIL_USERNAME/{GMAIL_USERNAME}/g" /var/spool/mail/.muttrc'.format(GMAIL_USERNAME=config['GMAIL_USERNAME']))
os.system('sed -ie "s/GMAIL_PASSWORD/{GMAIL_PASSWORD}/g" /var/spool/mail/.muttrc'.format(GMAIL_PASSWORD=config['GMAIL_PASSWORD']))

crontab_template = "*/15 * * * * mail /usr/bin/python36 /files/code/automail.py {parser} {emails}\n"
crontab = ""

for parser in config['parsers']:
    crontab += crontab_template.format(
        parser = parser['name'],
        emails = parser['emails']
    )

with open('/etc/cron.d/automail', 'wb') as file:
    file.write(crontab.encode('UTF-8'))

os.system('echo -e "Startup at: $(date)" > /var/log/cron.log')
os.system("crond && tail -f /var/log/cron.log")