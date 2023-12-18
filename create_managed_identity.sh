#!/bin/bash

# Variables
RESOURCE_GROUP="kalidynamics2024"
IDENTITY_NAME="MyNewManagedIdentity"

# Login to Azure (uncomment the next line if you need to login interactively)
# az login

# Create a new managed identity
echo "Creating a new managed identity..."
identity=$(az identity create --name $IDENTITY_NAME --resource-group $RESOURCE_GROUP)
clientId=$(echo $identity | jq -r '.clientId')
principalId=$(echo $identity | jq -r '.principalId')

# Assign the "Owner" role to the managed identity for the subscription
# WARNING: This grants full admin access. Use with caution.
echo "Assigning 'Owner' role to the managed identity..."
subscriptionId=$(az account show --query 'id' -o tsv)
az role assignment create --assignee $principalId --role "Owner" --scope "/subscriptions/$subscriptionId"

# Output the client ID and secret
echo "Managed Identity created successfully."
echo "Client ID: $clientId"

# Note: Managed identities do not have secrets like Service Principals. They use Azure AD to authenticate.
