import json
 
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
 
def get_bearer_token(credentials, url):
    response = requests.post(url, data=credentials)
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Failed to get token. Status code: {response.status_code}")
 
def make_api_call(api_details, token):
    url = api_details["url"]
    method = api_details.get("method", "GET").upper()
    headers = api_details["headers"]
    headers["Authorization"] = f"Bearer {token}"
 
    if method == "POST":
        body = api_details.get("body", {})
        response = requests.post(url, headers=headers, json=body)
    elif method == "GET":
        response = requests.get(url, headers=headers)
    else:
        raise ValueError(f"Unsupported method: {method}")
 
    return response
 
def main():
    credentials_file = "credentials.json"
    api_details_file = "api_details.json"
 
    token_url = "https://login.microsoftonline.com/orxhemiprodb2c.onmicrosoft.com/oauth2/token"
 
    try:
        credentials = read_json(credentials_file)
        apis = read_json(api_details_file)
 
        token = get_bearer_token(credentials, token_url)
 
        for api_key, api_info in apis.items():
            if api_info.get("status", "no").lower() == "yes":
                response = make_api_call(api_info, token)
                print(f"{api_key} Response Status Code: {response.status_code}")
                print(f"{api_key} Response Body: {response.json() if response.content else 'No content'}")
            else:
                print(f"Skipping {api_key} as status is not 'yes'.")
 
    except Exception as e:
        print(f"An error occurred: {e}")
 
if __name__ == "__main__":
    main()
