import argparse
import requests

#Command line argument handling
parser = argparse.ArgumentParser(description="Fetch a GitHub user's recent activity.")
parser.add_argument('username', type=str, help='GitHub username')
args = parser.parse_args()

def fetch_github_activity(username):
    url = f"https://api.github.com/users/{username}/events"
    response = requests.get(url)

    #handle response status codes
    if response