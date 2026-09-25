def validate_users(df):
    print("\nValidating users data...")

    if df.empty:
        raise ValueError("Users DataFrame is empty.")

    if df["user_id"].isnull().any():
        raise ValueError("Users contain NULL user_id.")

    if df["user_id"].duplicated().any():
        raise ValueError("Duplicate user_id found.")

    if df["email"].isnull().any():
        raise ValueError("Users contain NULL email.")

    print("Users validation passed.")


def validate_posts(df):
    print("\nValidating posts data...")

    if df.empty:
        raise ValueError("Posts DataFrame is empty.")

    if df["post_id"].isnull().any():
        raise ValueError("Posts contain NULL post_id.")

    if df["post_id"].duplicated().any():
        raise ValueError("Duplicate post_id found.")

    if df["user_id"].isnull().any():
        raise ValueError("Posts contain NULL user_id.")

    print("Posts validation passed.")