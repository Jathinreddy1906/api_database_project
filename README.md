# API to PostgreSQL Data Ingestion

A Python ETL example that fetches users and posts from the JSONPlaceholder API,
transforms the responses into pandas DataFrames, validates the data, and loads
it into PostgreSQL.

## Pipeline

1. Extract users and posts from `https://jsonplaceholder.typicode.com`.
2. Transform each response into a tabular format.
3. Validate required IDs, email values, and duplicate IDs.
4. Insert or update the records in PostgreSQL.

## Requirements

- Python 3
- PostgreSQL

Install the Python dependencies:

```bash
python -m pip install requests pandas psycopg2-binary
```

## Database setup

Create the database `api_reporting_db`, then connect to it and create the tables:

```sql
CREATE TABLE users (
    user_id BIGINT PRIMARY KEY,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    city TEXT NOT NULL
);

CREATE TABLE posts (
    post_id BIGINT PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(user_id),
    title TEXT NOT NULL,
    body TEXT NOT NULL
);
```

The connection settings are in `src/database.py`. Update them to match your
local PostgreSQL host, port, database, user, and password. Do not commit real
database credentials.

## Run

From the repository root, run:

```bash
python src/main.py
```

The script fetches both API resources, validates the returned data, and loads
users before posts so the post-to-user foreign key is satisfied. Re-running
the script updates existing rows by their IDs.

## Project layout

```text
src/
  main.py           # Runs the ingestion pipeline
  api_extractor.py  # Fetches users and posts from the API
  transform.py      # Converts API responses to DataFrames
  validation.py     # Validates transformed data
  load_data.py      # Upserts records into PostgreSQL
  database.py       # Creates PostgreSQL connections
```
