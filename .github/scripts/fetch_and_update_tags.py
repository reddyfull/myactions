import os
import requests
import json
from collections import defaultdict

def get_repo_from_url(url):
    parts = url.split('/')
    user, repo = parts[3], parts[4]
    return user, repo

def get_tags(token, user, repo):
    headers = {"Authorization": f"token {token}"}
    url = f"https://api.github.com/repos/{user}/{repo}/tags"
    response = requests.get(url, headers=headers)
    if response.ok:
        return response.json()
    else:
        raise Exception(f"Failed to fetch tags: {response.content}")

def organize_tags(tags):
    organized_tags = defaultdict(list)
    for tag in tags:
        parts = tag["name"].split('-')
        if len(parts) > 1:
            # Assuming the format is like Release-V0.1-20231219211000
            parent_version = '-'.join(parts[:2])  # This will be Release-V0.1
            organized_tags[parent_version].append(tag["name"])
        else:
            organized_tags[tag["name"]].append(tag["name"])
    return organized_tags

def main():
    token = os.getenv('GITHUB_TOKEN')
    if not token:
        raise Exception("GitHub token not found")

    user, repo = get_repo_from_url("https://github.com/reddyfull/myactions")
    tags = get_tags(token, user, repo)

    organized_data = organize_tags(tags)

    file_path = ".github/data/tags.json"
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, "w") as file:
        json.dump(organized_data, file, indent=4)

if __name__ == "__main__":
    main()
