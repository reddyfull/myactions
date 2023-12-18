import os
import azure.identity
import azure.mgmt.frontdoor
import azure.mgmt.cdn

# Get the client ID, client secret, tenant ID, and subscription ID from GitHub Secrets
client_id = os.environ["client_id"]
client_secret = os.environ["client_secret"]
tenant_id = os.environ["tenant_id"]
subscription_id = os.environ["subscription_id"]

# Create a service principal credential
credentials = azure.identity.ClientSecretCredential(
    client_id=client_id,
    client_secret=client_secret,
    tenant_id=tenant_id,
)

# Create a client for the Azure Front Door service
frontdoor_client = azure.mgmt.frontdoor.FrontDoorManagementClient(
    credential=credentials, subscription_id=subscription_id
)

# Create a client for the Azure CDN service
cdn_client = azure.mgmt.cdn.CdnManagementClient(credential=credentials, subscription_id=subscription_id)

# Create a Front Door resource
front_door_properties = {
    "sku": "Premium_V2",
    "waf_configuration": {
        "enabled": True,
        "rule_sets": ["AzureManagedRuleSet_FrontDoor_WebAttacks"],
    },
    "cdn_configuration": {
        "profile_name": "my-cdn-profile",
    },
}

front_door_operation = frontdoor_client.begin_create_or_update_front_door_with_cdn_profile(
    resource_group_name="my-resource-group",
    front_door_name="my-front-door",
    front_door_properties=front_door_properties,
)

# Wait until the Front Door resource is created
front_door_operation.wait_for_completion()

# Print the Front Door URL
print(front_door_operation.result().properties.frontend_endpoints[0].url)
