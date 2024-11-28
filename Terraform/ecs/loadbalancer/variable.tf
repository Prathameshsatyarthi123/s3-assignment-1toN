variable "regions" {
  type = map(any)
}
variable "product" {
  default = "casp"
}
variable "environment" {
  type = any
}