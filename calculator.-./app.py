from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
   result = "0"


   if request.method == "POST":
       current = request.form.get("result", "0")
       button = request.form.get("button")


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


   return render_template("index.html", result=result)

