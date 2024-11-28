regions = {
  prod = "us-east-1"
}
environment = {
  prod = {
    ecr_config = {
      repository_name                 = "s3-backend-image-repo"
      repository_image_tag_mutability = "MUTABLE"
    }
  }
}
