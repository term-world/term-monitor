from flask import Flask
import subprocess
from daemonize import Daemonize

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Hello World</h1>"

@app.route("/pm2")
def pm2():
    return subprocess.run(["pm2", "list"], capture_output=True).stdout

def main():
    app.run()

if __name__ == "__main__":
    myname = os.path.basename(sys.argv[0])
    pidfile = '/tmp/%s' % myname  # any name
    daemon = Daemonize(app=myname, pid=pidfile, action=main)
    daemon.start()