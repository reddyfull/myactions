import sys
import json

def update_configuration(endpoint_id, region):
    with open('endpoints_config.json', 'r') as file:
        config = json.load(file)
    
    for endpoint in config["endpoints"]:
        if endpoint["id"] == endpoint_id:
            for backend in endpoint["backends"]:
                if region == "both":
                    backend["enabled"] = True
                else:
                    backend["enabled"] = (backend["name"].lower() == region)
            break

    with open('endpoints_config.json', 'w') as file:
        json.dump(config, file, indent=4)

if __name__ == "__main__":
    endpoint_id_input = sys.argv[1]
    region_input = sys.argv[2].lower()
    update_configuration(endpoint_id_input, region_input)
