terraform {
  backend "s3" {
    bucket = "project-casp-remote-state"
    key    = "service.tfstate"
    region = "us-east-1"
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "4.22.0"
    }
  }
}

provider "aws" {
  region = local.region
} 
