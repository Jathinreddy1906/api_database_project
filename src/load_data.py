from database import get_connection


def load_users(df):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO users
        (user_id, name, username, email, city)
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (user_id)
        DO UPDATE SET
            name = EXCLUDED.name,
            username = EXCLUDED.username,
            email = EXCLUDED.email,
            city = EXCLUDED.city;
    """

    for _, row in df.iterrows():

        cursor.execute(
            query,
            (
                int(row["user_id"]),
                row["name"],
                row["username"],
                row["email"],
                row["city"]
            )
        )

    connection.commit()

    cursor.close()
    connection.close()

    print("Users loaded successfully.")


def load_posts(df):

    connection = get_connection()
    cursor = connection.cursor()

    query = """
        INSERT INTO posts
        (post_id, user_id, title, body)
        VALUES (%s, %s, %s, %s)
        ON CONFLICT (post_id)
        DO UPDATE SET
            user_id = EXCLUDED.user_id,
            title = EXCLUDED.title,
            body = EXCLUDED.body;
    """

    for _, row in df.iterrows():

        cursor.execute(
            query,
            (
                int(row["post_id"]),
                int(row["user_id"]),
                row["title"],
                row["body"]
            )
        )

    connection.commit()

    cursor.close()
    connection.close()

    print("Posts loaded successfully.")