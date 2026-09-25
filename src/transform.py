import pandas as pd


def transform_users(users):

    records = []

    for user in users:
        records.append({
            "user_id": user["id"],
            "name": user["name"],
            "username": user["username"],
            "email": user["email"],
            "city": user["address"]["city"]
        })

    df = pd.DataFrame(records)

    return df


def transform_posts(posts):

    records = []

    for post in posts:
        records.append({
            "post_id": post["id"],
            "user_id": post["userId"],
            "title": post["title"],
            "body": post["body"]
        })

    df = pd.DataFrame(records)

    return df