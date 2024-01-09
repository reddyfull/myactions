from azure.appconfiguration import AzureAppConfigurationClient, ConfigurationSetting
import os
import json

# Retrieve connection string from environment variable
connection_string = os.getenv('APP_CONFIG_CONNECTION')

if not connection_string:
    raise ValueError("Connection string not found in environment variables. Please check your GitHub secrets configuration.")

config_client = AzureAppConfigurationClient.from_connection_string(connection_string)

# Load configuration data from JSON file
with open('config.json') as config_file:
    config_data = json.load(config_file)

# Push configurations to Azure App Configuration
for key, value in config_data.items():
    setting = ConfigurationSetting(key=key, value=value)
    config_client.set_configuration_setting(setting)

print("Configurations pushed to Azure App Configuration.")
