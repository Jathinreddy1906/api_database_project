import requests # pyright: ignore[reportMissingModuleSource]


def get_users():

    url = "https://jsonplaceholder.typicode.com/users"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("Error fetching users:", error)
        return []


def get_posts():

    url = "https://jsonplaceholder.typicode.com/posts"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        return response.json()

    except requests.exceptions.RequestException as error:
        print("Error fetching posts:", error)
        return []