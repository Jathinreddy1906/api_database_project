from api_extractor import get_users, get_posts
from transform import transform_users, transform_posts
from validation import validate_users, validate_posts
from load_data import load_users, load_posts


def main():

    print("=" * 50)
    print("API TO DATABASE DATA INGESTION")
    print("=" * 50)

    # 1. Extract
    print("\n1. Extracting data from API...")

    users = get_users()
    posts = get_posts()

    print(f"Users extracted: {len(users)}")
    print(f"Posts extracted: {len(posts)}")

    if not users or not posts:
        print("No data received from API.")
        return

    # 2. Transform
    print("\n2. Transforming data...")

    users_df = transform_users(users)
    posts_df = transform_posts(posts)

    print(f"Users transformed: {len(users_df)}")
    print(f"Posts transformed: {len(posts_df)}")

    # 3. Validate
    print("\n3. Validating data...")

    validate_users(users_df)
    validate_posts(posts_df)

    # 4. Load
    print("\n4. Loading data into PostgreSQL...")

    load_users(users_df)
    load_posts(posts_df)

    print("\n5. Data ingestion completed successfully.")

    print("=" * 50)


if __name__ == "__main__":
    main()