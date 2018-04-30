## automail

automail - Web page parser & email sender *via mutt.  
Parse proper web page and get information about promotion.

## Structure: 
* automail/terraform -> AWS Terraform code for server backend 
* automail/ansible   -> Ansible code for deploying purpose
* automail/code      -> Python project code

## Setup  

1. `git clone https://github.com/Vermibus/automail.git`
2. Inside automail/terraform:
   1. automail ec2 is taking the key with name 'my-key' -> change if other name used for key-pair
   2. provide AWS credencials via environment variables
   3. `terraform init`
   4. `terraform apply`
   5. copy the IP address of automail instance from output
3. Inside automail/ansible:
   1. Populate group_vars/all.yml:
      * gmail_name, _username, _password with proper gmail account credencials
      * parsers[*]['emails'] - space separated email addresses eg: "e1@m.com e2@m.com"
   2. Paste automail instance IP address into inventory file
   3. `ansible-playbook -i inventory play.yml`
4. Done
