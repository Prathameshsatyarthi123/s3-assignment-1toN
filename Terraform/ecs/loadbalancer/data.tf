data "terraform_remote_state" "vpc" {
  backend = "s3"
  config = {
    bucket = "project-casp-remote-state"
    key    = "vpc.tfstate"
    region = "us-east-1"
  }
  workspace = local.environment
}
