terraform {
  backend "s3" {
    bucket = "static-permament-bucket"
    key    = "tfstates/automail/terraform.tfstate"
    region = "eu-west-1"
  }
}
