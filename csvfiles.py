import pandas as pd
import socket

# Initialize an empty list to store the results
results = []

# Read the CSV file into a DataFrame
try:
    df = pd.read_csv('query_data.csv')  # Replace with your actual input file path
    print(f"Original DataFrame has {len(df)} rows")
except Exception as e:
    print(f"Error reading CSV: {e}")

# Filter based on your conditions
try:
    filtered_df = df[
        (df['httpStatusCode_d'] == 301) &
        (df['requestUri_s'] == 'https://pharmacy.optum.com:443/') &
        (df['routingRuleName_s'] == 'pharmacy-routing-rule')
    ]
    print(f"Filtered DataFrame has {len(filtered_df)} rows")
except Exception as e:
    print(f"Error during filtering: {e}")

# Drop NaN values in the 'clientIp_s' column
try:
    filtered_df = filtered_df.dropna(subset=['clientIp_s'])
    print(f"DataFrame after dropping NaNs has {len(filtered_df)} rows")
except Exception as e:
    print(f"Error dropping NaNs: {e}")

# Convert IP addresses to string type
try:
    filtered_df['clientIp_s'] = filtered_df['clientIp_s'].astype(str)
except Exception as e:
    print(f"Error during type conversion: {e}")

# Perform reverse DNS lookup
try:
    for ip in filtered_df['clientIp_s'].unique():
        domain_name = socket.getfqdn(ip)
        results.append({'IP Address': ip, 'Domain Name': domain_name})
except Exception as e:
    print(f"Error during reverse DNS lookup: {e}")

# Convert the list of results to a DataFrame
result_df = pd.DataFrame(results)

# Save the results to a CSV file
try:
    result_df.to_csv('output.csv', index=False)
    print("Output saved to output.csv")
except Exception as e:
    print(f"Error saving output: {e}")

print("Debugging information complete.")
