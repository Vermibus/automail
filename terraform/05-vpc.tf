resource "aws_vpc" "core" {
  cidr_block = "10.24.0.0/16"

  tags {
    Name = "core_vpc"
  }
}
