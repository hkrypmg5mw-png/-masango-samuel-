provider "aws" {
  region = "us-east-1"
}

resource "aws_db_instance" "default" {
  allocated_storage    = 20
  db_name              = "mchfus"
  engine               = "postgres"
  engine_version       = "15"
  instance_class       = "db.t3.micro"
  username             = "postgres"
  password             = var.db_password
  skip_final_snapshot  = true
}

resource "aws_elastic_beanstalk_application" "tacos" {
  name        = "mch-fus"
  description = "Maternal and Child Health Follow-Up System"
}

resource "aws_elastic_beanstalk_environment" "tfenv" {
  name                = "mch-fus-prod"
  application         = aws_elastic_beanstalk_application.tacos.name
  solution_stack_name = "64bit Amazon Linux 2 v3.5.8 running Docker"

  setting {
    namespace = "aws:elasticbeanstalk:application:environment"
    name      = "DATABASE_URL"
    value     = "postgres://postgres:${var.db_password}@${aws_db_instance.default.endpoint}/mchfus"
  }
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}
