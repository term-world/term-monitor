from flask import Flask
import subprocess
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/pm2")
def pm2():
    num_newlines = 0
    length = 50
    lines = []
    with open("../.pm2/pm2.log", 'rb') as f:
        try:
            f.seek(-2, os.SEEK_END)
            while num_newlines < length:
                f.seek(-2, os.SEEK_CUR)
                if f.read(1) == b'\n':
                    num_newlines += 1
                    lines.append(f.readline().decode())
        except OSError:
            f.seek(0)
        last_line = f.readline().decode()
    return lines
    # return subprocess.run(["pm2", "logs", "--json", "--timestamp", "--nostream", "--lines", "50"], capture_output=True).stdout

def main():
    app.run("0.0.0.0")

if __name__ == "__main__":
    main()