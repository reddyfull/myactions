provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "rg" {
  name     = "kalidynamics2024"
  location = "Global"
}

variable "frontdoor_config" {
  type = any
  default = jsondecode(file("${path.module}/frontdoor_config.json"))
}

resource "azurerm_cdn_frontdoor_profile" "fd_profile" {
  name                = "fdpremkalidynamics2024"
  resource_group_name = azurerm_resource_group.rg.name
  sku                 = "Premium_AzureFrontDoor"

  dynamic "endpoint" {
    for_each = var.frontdoor_config["endpoints"]
    content {
      name      = endpoint.value.name
      host_name = endpoint.value.host_name
    }
  }

  dynamic "origin" {
    for_each = var.frontdoor_config["origins"]
    content {
      name      = origin.value.name
      host_name = origin.value.host_name
    }
  }

  dynamic "routing_rule" {
    for_each = var.frontdoor_config["routing_rules"]
    content {
      name                  = routing_rule.value.name
      accepted_protocols    = routing_rule.value.accepted_protocols
      patterns_to_match     = routing_rule.value.patterns_to_match
      frontend_endpoints    = routing_rule.value.frontend_endpoints
      forwarding_protocol   = routing_rule.value.forwarding_protocol
      # Additional routing rule configurations
      # ...
    }
  }
}
