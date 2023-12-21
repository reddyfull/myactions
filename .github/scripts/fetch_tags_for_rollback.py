import sys
import json
import os

def main(parent_version):
    file_path = ".github/data/tags.json"
    if not os.path.exists(file_path):
        print("::error::Tags file not found.")
        sys.exit(1)

    with open(file_path, 'r') as file:
        tags_data = json.load(file)
    
    child_tags = tags_data.get(parent_version, [])
    print("::set-output name=childTags::" + json.dumps(child_tags))

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("::error::Parent version argument is required")
        sys.exit(1)

    main(sys.argv[1])
