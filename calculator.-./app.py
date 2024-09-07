from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method != "POST":
        return render_template("index.html", result=10)
    value = request.form.get("number")
    return render_template("index.html", result=value)
