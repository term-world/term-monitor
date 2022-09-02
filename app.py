from flask import Flask
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/pm2")
def pm2():
    return subprocess.run(["pm2", "list"], capture_output=True).stdout

if __name__ == "__main__":
    app.run()