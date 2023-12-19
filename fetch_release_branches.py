# fetch_release_branches.py
import requests
import os
import json

def fetch_release_branches(repo):
    url = f"https://api.github.com/repos/{repo}/branches"
    response = requests.get(url)
    branches = response.json()
    release_branches = [branch['name'] for branch in branches if branch['name'].startswith('release-')]
    return release_branches

if __name__ == "__main__":
    repo = os.environ.get('GITHUB_REPOSITORY')
    branches = fetch_release_branches(repo)
    print(json.dumps(branches))
