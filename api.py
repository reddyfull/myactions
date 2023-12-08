import os
import json
import requests

def get_api_config():
    api_config_json = os.getenv("API_CONFIG_JSON")
    if not api_config_json:
        raise ValueError("API configuration not found in environment variables")
    return json.loads(api_config_json)

def make_api_request(api_details):
    url = api_details["url"]
    method = api_details["method"]
    headers = api_details.get("headers", {})
    body = api_details.get("body", {})

    if method.upper() == "GET":
        response = requests.get(url, headers=headers)
    elif method.upper() == "POST":
        response = requests.post(url, headers=headers, json=body)
    else:
        raise ValueError(f"Unsupported HTTP method: {method}")

    return response

def main():
    api_config = get_api_config()

    for api_name, api_details in api_config.items():
        if api_details.get("status", "").lower() == "yes":
            response = make_api_request(api_details)
            print(f"Response from {api_name}: {response.status_code}")
            print(f"Response body: {response.json()}")
        else:
            print(f"Skipping {api_name} as its status is not 'yes'.")

if __name__ == "__main__":
    main()
