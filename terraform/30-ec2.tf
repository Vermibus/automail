resource "aws_instance" "automail" {
  ami                    = "${data.aws_ami.automail.id}"
  instance_type          = "t2.micro"
  subnet_id              = "${aws_subnet.pub_subnet.id}"
  vpc_security_group_ids = ["${aws_security_group.automail.id}"]
  key_name               = "my-key"

  root_block_device {
    volume_size           = 8
    volume_type           = "gp2"
    delete_on_termination = "true"
  }

  tags {
    Name = "automail"
  }
}
