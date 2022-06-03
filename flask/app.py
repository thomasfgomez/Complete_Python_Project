from flask import Flask, render_template
import socket

app = Flask(__name__)


@app.route("/")
def home():
    print("This is your landing page to your Flask project! :)")
    return f"Container ID: {socket.gethostname()}"


@app.route("/saludo")
def saludo():
    return render_template('index.html')
    



