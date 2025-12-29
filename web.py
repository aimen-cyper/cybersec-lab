from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/phishing")
def phishing():
    return render_template("phishing_demo.html")

@app.route("/ip")
def ip():
    return render_template("ip.html")

@app.route("/defense")
def defense():
    return render_template("defense.html")

@app.route("/checklist")
def checklist():
    return render_template("checklist.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)