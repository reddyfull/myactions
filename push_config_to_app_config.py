from azure.appconfiguration import AzureAppConfigurationClient
import os
import json

# Retrieve connection string from environment variable
connection_string = os.getenv('APP_CONFIG_CONNECTION')

config_client = AzureAppConfigurationClient.from_connection_string(connection_string)

# Load configuration data from JSON file
with open('config.json') as config_file:
    config_data = json.load(config_file)

# Push configurations to Azure App Configuration
for key, value in config_data.items():
    config_client.set_configuration_setting(key=key, value=value)

print("Configurations pushed to Azure App Configuration.")
