# Copilot: Refer to sla.md for service level agreement requirements
# Copilot: Select the SKU for this resource from sku_mapping.json using its defined priority
# Copilot: For P1 priority, enable multi-AZ with three availability zones if this resource supports it.

resource "azurerm_application_gateway" "example" {
    name                = "example-appgateway"
    resource_group_name = azurerm_resource_group.example.name
    location            = azurerm_resource_group.example.location
    sku {
        name     = "Standard_v2"
        tier     = "Standard_v2"
        capacity = 3
    }

    gateway_ip_configuration {
        name      = "my-gateway-ip-configuration"
        subnet_id = azurerm_subnet.example.id
    }

    frontend_port {
        name = "frontendport"
        port = 80
    }

    frontend_ip_configuration {
        name                 = "frontendipconfiguration"
        public_ip_address_id = azurerm_public_ip.example.id
    }

    backend_address_pool {
        name = "backendaddresspool"
    }

    backend_http_settings {
        name                  = "backendhttpsettings"
        cookie_based_affinity = "Disabled"
        port                  = 80
        protocol              = "Http"
        request_timeout       = 20
    }

    http_listener {
        name                           = "httplistener"
        frontend_ip_configuration_name = "frontendipconfiguration"
        frontend_port_name             = "frontendport"
        protocol                       = "Http"
    }

    request_routing_rule {
        name                       = "requestroutingrule"
        rule_type                  = "Basic"
        http_listener_name         = "httplistener"
        backend_address_pool_name  = "backendaddresspool"
        backend_http_settings_name = "backendhttpsettings"
    }

    tags = {
        environment = "Production"
    }
}
resource "azurerm_kubernetes_cluster" "example" {
    name                = "example-aks"
    location            = azurerm_resource_group.example.location
    resource_group_name = azurerm_resource_group.example.name
    dns_prefix          = "exampleaks"

    default_node_pool {
        name       = "default"
        node_count = 3
        vm_size    = "Standard_DS2_v2"
        vnet_subnet_id = azurerm_subnet.example.id
    }

    identity {
        type = "SystemAssigned"
    }

    network_profile {
        network_plugin    = "azure"
        network_policy    = "azure"
        load_balancer_sku = "standard"
        outbound_type     = "userDefinedRouting"
    }

    api_server_authorized_ip_ranges = ["10.0.0.0/8"]

    role_based_access_control {
        enabled = true
    }

    addon_profile {
        oms_agent {
            enabled = true
            log_analytics_workspace_id = azurerm_log_analytics_workspace.example.id
        }
    }

    tags = {
        environment = "Production"
    }
}