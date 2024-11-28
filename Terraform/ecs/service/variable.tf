variable "regions" {
  type = map(any)
}
variable "product" {
  default = "crasp"
}
variable "environment" {
  type = any
}