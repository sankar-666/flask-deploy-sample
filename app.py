from flask import Flask, render_template
from database import *

app = Flask(__name__)

@app.route("/")
def index():
    q = "select * from sample"
    name = select(q)[0]["name"]
    return render_template("index.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)