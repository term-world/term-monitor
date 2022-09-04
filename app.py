from flask import Flask
import subprocess
import os, io

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/pm2")
def pm2():
    n = 50
    proc = subprocess.Popen(['tail', "../.pm2/pm2.log", '-n', str(n), ], stdout=subprocess.PIPE)
    lines = []
    for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"):  # or another encoding
        lines.append(line)
    return lines
    # return subprocess.run(["pm2", "logs", "--json", "--timestamp", "--nostream", "--lines", "50"], capture_output=True).stdout

@app.route("/docker/list")
def docker_ps():
    proc = subprocess.run(["docker", "ps", "-a"], capture_output=True).stdout
    print(repr(proc))
    return proc

def main():
    app.run("0.0.0.0")

if __name__ == "__main__":
    main()