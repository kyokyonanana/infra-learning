import os

import psycopg2
from flask import Flask

app = Flask(__name__)


def run(statements):
    conn = psycopg2.connect(
        host=os.environ["DB_HOST"],
        dbname=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        connect_timeout=3,
    )
    try:
        with conn, conn.cursor() as cur:
            for sql in statements:
                cur.execute(sql)
            return cur.fetchone()
    finally:
        conn.close()


@app.route("/")
def index():
    row = run([
        "CREATE TABLE IF NOT EXISTS hits (id serial PRIMARY KEY, at timestamptz DEFAULT now())",
        "INSERT INTO hits DEFAULT VALUES",
        "SELECT count(*) FROM hits",
    ])
    return f"Hello from compose! hits={row[0]}\n"


@app.route("/health")
def health():
    return "ok\n"


@app.route("/health/db")
def health_db():
    run(["SELECT 1"])
    return "db ok\n"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
