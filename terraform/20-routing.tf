resource "aws_internet_gateway" "core_igw" {
  vpc_id = "${aws_vpc.core.id}"

  tags {
    Name = "core_igw"
  }
}

resource "aws_route_table" "core_rt" {
  vpc_id = "${aws_vpc.core.id}"

  tags {
    Name = "core_route_table"
  }

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = "${aws_internet_gateway.core_igw.id}"
  }
}

resource "aws_route_table_association" "pub_rt" {
  subnet_id      = "${aws_subnet.pub_subnet.id}"
  route_table_id = "${aws_route_table.core_rt.id}"
}
