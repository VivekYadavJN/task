from flask import Flask
import getpass
import time
import subprocess
import pytz
from datetime import datetime

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Vivek Yadav"
    username = getpass.getuser()
    ist = pytz.timezone('Asia/Kolkata')
    time_now = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')
    top_output = subprocess.getoutput("top -b -n 1 | head -n 10")

    return f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time (IST): {time_now}</h2>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
