from azure.identity import DefaultAzureCredential
from azure.mgmt.frontdoor import FrontDoorManagementClient
import json
import sys

# Set your Azure subscription ID, resource group, and Front Door name
subscription_id = 'Y217d2bdc-2706-4aa7-be71-457045f1baba'
resource_group = 'kalidynamics2024'
front_door_name = 'kalidynamics2024'

def main(endpoint_id, region):
    with open('endpoints_config.json', 'r') as file:
        config = json.load(file)

    # Find the specified endpoint and update its backends
    for endpoint in config["endpoints"]:
        if endpoint["id"] == endpoint_id:
            for backend in endpoint["backends"]:
                if region == "both":
                    backend["enabled"] = True
                else:
                    backend["enabled"] = (backend["name"].lower() == region)
            break

    # Use Azure SDK to update the Front Door configuration
    credential = DefaultAzureCredential()
    client = FrontDoorManagementClient(credential, subscription_id)
    
    front_door = client.front_doors.get(resource_group, front_door_name)
    # Update the Front Door configuration based on the updated endpoints_config.json
    # ...

    client.front_doors.begin_create_or_update(resource_group, front_door_name, front_door).result()
    print(f'Azure Front Door configuration updated for endpoint {endpoint_id}.')

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python update_frontdoor.py <endpoint_id> <region>')
        sys.exit(1)

    main(sys.argv[1], sys.argv[2])
