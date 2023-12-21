import requests

def get_user_info(token):
    headers = {'Authorization': f'token {token}'}
    response = requests.get('https://api.github.com/user', headers=headers)
    
    if response.ok:
        return response.json()
    else:
        return "Error: Unable to fetch user data"

# Replace 'your_token_here' with your actual token
my_token = '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'
user_info = get_user_info(my_token)
print(user_info)
