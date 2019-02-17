## automail

automail - Web page parser & email sender *via mutt.  
Parse proper web page and get information about promotion.

## Structure: 
* automail/code      -> Python project code
* automail/docker    -> Docker image capable of running automail via crond 
* automail/terraform -> Old Implementation: AWS Terraform code for server backend 
* automail/ansible   -> Old Implementation: Ansible code for deploying purpose

## Setup  

1. `git clone https://github.com/Vermibus/automail.git`
2. Populate config.yml with emails and correct credentials for GMAIL account (remember to enable IMAP access)
3. make build
4. make run 
