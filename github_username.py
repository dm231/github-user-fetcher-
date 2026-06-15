import requests
import json


def fetch_github(username):

    # User API URL
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    # Handle invalid username
    if response.status_code == 404:
        print("❌ User not found!")
        return

    data = response.json()

    # Display user details
    print("\n===== GitHub User Details =====")

    print(f"Name: {data.get('name')}")
    print(f"Username: {data.get('login')}")
    print(f"Bio: {data.get('bio')}")
    print(f"Followers: {data.get('followers')}")
    print(f"Following: {data.get('following')}")
    print(f"Public Repositories: {data.get('public_repos')}")
    print(f"Account Created: {data.get('created_at')}")

    # Fetch repositories
    repo_url = data.get("repos_url")

    repo_response = requests.get(repo_url)

    repo_data = repo_response.json()

    # Sort repositories by stars
    sorted_repos = sorted(
        repo_data,
        key=lambda repo: repo["stargazers_count"],
        reverse=True
    )

    # Display top 5 repositories
    print("\n===== Top 5 Repositories =====")

    for repo in sorted_repos[:5]:

        print(
            f"⭐ {repo['name']} "
            f"(Stars: {repo['stargazers_count']})"
        )

    # Save user data to JSON file
    with open(f"{username}.json", "w") as file:

        json.dump(data, file, indent=4)

    print(f"\n✅ Data saved to {username}.json")


# User input
username = input("Enter Username: ")

fetch_github(username)import requests
import json


def fetch_github(username):

    # User API URL
    url = f"https://api.github.com/users/{username}"

    response = requests.get(url)

    # Handle invalid username
    if response.status_code == 404:
        print("❌ User not found!")
        return

    data = response.json()

    # Display user details
    print("\n===== GitHub User Details =====")

    print(f"Name: {data.get('name')}")
    print(f"Username: {data.get('login')}")
    print(f"Bio: {data.get('bio')}")
    print(f"Followers: {data.get('followers')}")
    print(f"Following: {data.get('following')}")
    print(f"Public Repositories: {data.get('public_repos')}")
    print(f"Account Created: {data.get('created_at')}")

    # Fetch repositories
    repo_url = data.get("repos_url")

    repo_response = requests.get(repo_url)

    repo_data = repo_response.json()

    # Sort repositories by stars
    sorted_repos = sorted(
        repo_data,
        key=lambda repo: repo["stargazers_count"],
        reverse=True
    )

    # Display top 5 repositories
    print("\n===== Top 5 Repositories =====")

    for repo in sorted_repos[:5]:

        print(
            f"⭐ {repo['name']} "
            f"(Stars: {repo['stargazers_count']})"
        )

    # Save user data to JSON file
    with open(f"{username}.json", "w") as file:

        json.dump(data, file, indent=4)

    print(f"\n✅ Data saved to {username}.json")


# User input
username = input("Enter Username: ")

fetch_github(username)
