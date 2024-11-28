data "terraform_remote_state" "vpc" {
  backend = "s3"
  config = {
    bucket = "project-casp-remote-state"
    key    = "vpc.tfstate"
    region = "us-east-1"
  }
  workspace = local.environment
}

data "terraform_remote_state" "alb" {
  backend = "s3"
  config = {
    bucket = "project-casp-remote-state"
    region = "us-east-1"
    key    = "alb.tfstate"
  }
  workspace = local.environment
}

data "terraform_remote_state" "ecr" {
  backend = "s3"
  config = {
    bucket = "project-casp-remote-state"
    region = "us-east-1"
    key    = "ecr.tfstate"
  }
  workspace = local.environment
}

data "terraform_remote_state" "cluster" {
  backend = "s3"
  config = {
    bucket = "project-casp-remote-state"
    region = "us-east-1"
    key    = "cluster.tfstate"
  }
  workspace = local.environment
}

