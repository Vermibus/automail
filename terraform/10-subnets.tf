resource "aws_subnet" "pub_subnet" {
  vpc_id                  = "${aws_vpc.core.id}"
  cidr_block              = "10.24.20.0/24"
  map_public_ip_on_launch = "true"

  tags {
    Name = "pub_subnet"
  }
}
