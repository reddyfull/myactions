import json
from azure.keyvault.secrets import SecretClient
from azure.identity import ClientSecretCredential
from azure.core.exceptions import ResourceNotFoundError, HttpResponseError

# Load Azure credentials from file
with open('azure_credentials.json', 'r') as file:
    azure_credentials = json.load(file)
tenant_id = azure_credentials['tenantId']
client_id = azure_credentials['clientId']
client_secret = azure_credentials['clientSecret']

# Initialize the Azure Key Vault client
keyvault_name = 'kalidynamics2024'
kv_uri = f"https://{keyvault_name}.vault.azure.net/"
credential = ClientSecretCredential(tenant_id, client_id, client_secret)
client = SecretClient(vault_url=kv_uri, credential=credential)

# Load the decrypted JSON data
with open('keyvault.json') as file:
    secrets_data = json.load(file)

# Insert secrets as per JSON instructions
for secret_name, secret_value in secrets_data.get('insert', {}).items():
    try:
        existing_secret = None
        try:
            existing_secret = client.get_secret(secret_name)
        except ResourceNotFoundError:
            pass  # Secret doesn't exist, which is fine
        
        if not existing_secret or existing_secret.value != secret_value:
            client.set_secret(secret_name, secret_value)
            print(f"Secret '{secret_name}' set successfully.")
        else:
            print(f"Secret '{secret_name}' already exists with the same value. No action taken.")

    except HttpResponseError as e:
        print(f"Failed to set secret '{secret_name}'. Error: {e}")

# Delete secrets as per JSON instructions, if any
for secret_name in secrets_data.get('delete', []):
    try:
        client.begin_delete_secret(secret_name).result()
        print(f"Secret '{secret_name}' deleted successfully.")
    except ResourceNotFoundError:
        print(f"Secret '{secret_name}' not found. No action taken.")
    except HttpResponseError as e:
        print(f"Failed to delete secret '{secret_name}'. Error: {e}")
