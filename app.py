from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/pm2")
def pm2():
    return subprocess.run(["pm2", "logs", "--json", "--timestamp", "--nostream", "--lines", "50"], capture_output=True).stdout

def main():
    app.run("0.0.0.0")

if __name__ == "__main__":
    main()