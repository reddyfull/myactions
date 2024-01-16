provider "azurerm" {
  features {}
}

locals {
  endpoints_config = jsondecode(var.endpoints_config)
}

resource "azurerm_frontdoor" "frontdoor" {
  name                = "kalidynamics2024"
  resource_group_name = "kalidynamics2024-resource-group"
  location            = "Global"
  enforce_backend_pools_certificate_name_check = false

  dynamic "frontend_endpoint" {
    for_each = local.endpoints_config.endpoints

    content {
      name      = frontend_endpoint.value.name
      host_name = frontend_endpoint.value.name
      // Additional frontend endpoint properties
    }
  }

  dynamic "backend_pool" {
    for_each = { for endpoint in local.endpoints_config.endpoints : endpoint.name => endpoint.backends }

    content {
      name = backend_pool.value.name

      dynamic "backend" {
        for_each = backend_pool.value

        content {
          address     = backend.value.address
          host_header = backend.value.address
          enabled     = backend.value.enabled
          // Additional backend settings
        }
      }
    }
  }

  dynamic "routing_rule" {
    for_each = { for endpoint in local.endpoints_config.endpoints : endpoint.name => endpoint.routing_rules }

    content {
      name               = routing_rule.value.name
      frontend_endpoints = [routing_rule.key]
      backend_pool_name  = routing_rule.value.backend_pool_name
      // Additional routing rule settings
    }
  }
}
