from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/pm2")
def pm2():
    n = 50
    proc = subprocess.Popen(['tail', '-n', str(n), "../.pm2/pm2.log"], stdout=subprocess.PIPE)
    lines = proc.stdout.readlines()
    return lines
    # return subprocess.run(["pm2", "logs", "--json", "--timestamp", "--nostream", "--lines", "50"], capture_output=True).stdout

def main():
    app.run("0.0.0.0")

if __name__ == "__main__":
    main()