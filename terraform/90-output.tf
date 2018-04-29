output "automail_public_ip" {
  value = "${aws_instance.automail.public_ip}\n"
}
