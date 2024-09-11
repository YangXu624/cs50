from flask import Flask, render_template, redirect, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    result = "0"


    if request.method == "POST":
        current = request.form.get("result", "0")
        button = request.form.get("button")

        if button == "shift":
            return redirect("/shift")
        if button == "shift":
            return redirect("/alpha")

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

@app.route("/shift", methods=["GET", "POST"])
def shift():
    result = "0"


    if request.method == "POST":
        current = request.form.get("result", "0")
        button = request.form.get("button")

        if button == "shift":
            return redirect("/")
        if button == "alpha":
            return redirect("/alpha")

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


    return render_template("shift.html", result=result)


@app.route("/alpha", methods=["GET", "POST"])
def alpha():
    result = "0"


    if request.method == "POST":
        current = request.form.get("result", "0")
        button = request.form.get("button")

        if button == "shift":
            return redirect("/shift")
        if button == "alpha":
            return redirect("/")

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


    return render_template("alpha.html", result=result)
