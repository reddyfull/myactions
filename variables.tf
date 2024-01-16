variable "endpoints_config" {
  type = any
  default = jsondecode(file("${path.module}/endpoints_config.json"))
}
