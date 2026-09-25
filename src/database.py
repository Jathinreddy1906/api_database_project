import psycopg2  # pyright: ignore[reportMissingModuleSource]


def get_connection():

    connection = psycopg2.connect(
        host="localhost",
        port=5432,
        database="api_reporting_db",
        user="postgres",
        password="1234"
    )

    return connection
try:
    connection = get_connection()
    print("PostgreSQL connection successful!")

    connection.close()

except Exception as error:
    print("Database connection failed:")
    print(error)