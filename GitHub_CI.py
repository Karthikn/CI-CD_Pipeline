
import requests
import os

# GitHub repository details
REPO_OWNER = "Karthikn"  # Replace with your GitHub username
REPO_NAME = "CI-CD_Pipeline"  # Replace with your repository name
GITHUB_API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/commits"
#LAST_COMMIT_FILE = "/var/www/html/last_commit.txt"  # Path to store last commit
LAST_COMMIT_FILE = "/var/www/html/CI-CD_Pipeline/last_commit.txt"  # Path to store last commit


def get_latest_commit():
    response = requests.get(GITHUB_API_URL)
    if response.status_code == 200:
        commits = response.json()
        return commits[0]['sha']
    else:
        print(f"Failed to fetch commits: {response.status_code}")
        return None

def get_stored_commit():
    if os.path.exists(LAST_COMMIT_FILE):
        with open(LAST_COMMIT_FILE, "r") as file:
            return file.read().strip()
    return None

def update_stored_commit(sha):
    with open(LAST_COMMIT_FILE, "w") as file:
        file.write(sha)

def main():
    latest_commit = get_latest_commit()
    if not latest_commit:
        exit(1)
    stored_commit = get_stored_commit()
    if latest_commit != stored_commit:
        print("New changes detected.")
        update_stored_commit(latest_commit)
        exit(0)
    else:
        print("No new changes.")
        exit(1)

if __name__ == "__main__":
    main()

