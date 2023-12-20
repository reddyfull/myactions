import os
import requests

def main():
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise Exception("GitHub token not found")

    headers = {"Authorization": f"token {token}"}
    response = requests.get('https://api.github.com/user', headers=headers)

    if response.ok:
        user_data = response.json()
        print("User Login: ", user_data.get('login'))
        print("User ID: ", user_data.get('id'))
        print("User Name: ", user_data.get('name'))
        print("Number of Public Repos: ", user_data.get('public_repos'))
        # You can add more fields to print as needed
    else:
        print("Failed to fetch user data")

if __name__ == "__main__":
    main()
