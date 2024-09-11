from flask import Flask, render_template, redirect, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main():
    result = "0"


    if request.method == "POST":
        current = request.form.get("result", "0")
        button = request.form.get("button")

        if button == "shift":
            return redirect("/shift")

        if button == "C":
            result = "0"
        elif button == "←":
            if len(current) > 1:
                result = current[:-1]
            else:
                result = "0"
        elif button == "=":
            try:
                result = str(eval(current.replace("×", "*").replace("÷", "/")))
            except Exception:
                result = "Error"
        else:
            if current == "0":
                result = button
            else:
                result = current + button


    return render_template("main.html", result=result)

@app.route("/", methods=["GET", "POST"])
