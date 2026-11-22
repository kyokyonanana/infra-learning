import os
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return f"Hello again from container! version={os.environ.get('APP_VERSION', 'unknown')}\n"

@app.route("/health")
def health():
    return "ok\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
