import json
import requests

def read_json_from_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def get_api_config_from_env(env_var_name):
    api_config_json = os.getenv(env_var_name)
    if not api_config_json:
        raise ValueError(f"{env_var_name} not found in environment variables")
    return json.loads(api_config_json)

def make_api_call(api_details, credentials):
    # ... your logic for making API calls ...

def main():
    credentials = read_json_from_file('credentials.json')
    api_config = get_api_config_from_env('API_CONFIG_JSON')

    for api_key, api_details in api_config.items():
        if api_details.get("status", "").lower() == "yes":
            response = make_api_call(api_details, credentials)
            # Handle the response

if __name__ == "__main__":
    main()
