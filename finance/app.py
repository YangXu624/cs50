import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from datetime import datetime
from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    userinfo = db.execute("SELECT username, cash FROM users WHERE id=?", session['user_id'])
    stocks = db.execute("SELECT symbol, amount FROM stocks WHERE user_id=?", session['user_id'])
    for stock in stocks:
        look = lookup(stock['symbol'])
        stock['value'] = stock['amount'] * look['price']
    return render_template("index.html", userinfo = userinfo[0], stocks = stocks)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method != "POST":
        return render_template("buy.html")

    symbol = request.form.get("symbol")
    quantity = int(request.form.get("quantity"))

    if not (isinstance(quantity, int) and quantity > 0):
        return apology("Quantity has to be a positive integer")

    query = lookup(symbol)
    payment = query['price'] * quantity

    cash = db.execute("SELECT cash FROM users WHERE id=?", session['user_id'])
    dct = cash[0]
    amt = dct['cash']

    if payment > amt:
        return apology("Insufficient balance :(")
    else:
        amt -= payment
        db.execute("UPDATE users SET cash = ? WHERE id = ?", amt, session['user_id'])
        db.execute("INSERT INTO records (user_id, symbol, quantity, transaction_type, time) VALUES (?, ?, ?, ?, ?)", session['user_id'], symbol.upper(), quantity, 'BUY', datetime.now())

    stock = db.execute("SELECT amount FROM stocks WHERE user_id=? AND symbol=?", session['user_id'], symbol.upper())
    if stock == []:
        db.execute("INSERT INTO stocks (user_id, symbol, amount) VALUES (?, ?, ?)", session['user_id'], symbol.upper(), quantity)
    else:
        dct = stock[0]
        number = dct['amount'] + quantity
        db.execute("UPDATE stocks SET amount = ? WHERE user_id = ?", number, session['user_id'])

    return redirect("/")

@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    info = db.execute("SELECT symbol, quantity, transaction_type, time FROM records WHERE user_id = ?", session['user_id'])
    return render_template("history.html", info = info)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute(
            "SELECT * FROM users WHERE username = ?", request.form.get("username")
        )

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(
            rows[0]["hash"], request.form.get("password")
        ):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if not request.method == "POST":
        return render_template("quote.html")

    symbol = request.form.get("symbol")
    query = lookup(symbol)

    return render_template("quoted.html", query=query)


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if not request.method == "POST":
        return render_template("register.html")

    username = request.form.get("username")
    password = request.form.get("password")
    confirmation = request.form.get("confirmation")
    if password != confirmation:
        return apology("Passwords do not match!")
    try:
        db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", username, generate_password_hash(password))
        return redirect("/")
    except ValueError:
        return apology("Username already taken!")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method != "POST":
        symbols = []
        stocks = db.execute("SELECT symbol FROM stocks WHERE user_id=?", session['user_id'])
        for stock in stocks:
            symbols.append(stock['symbol'])
        return render_template("sell.html", symbols = symbols)
    else:
        if not request.form.get("symbol"):
            return apology("Select your stock")
        else:
            symbol = request.form.get("symbol")
        if not request.form.get("quantity"):
            return apology("Input quantity")
        else:
            quantity = int(request.form.get("quantity"))
            if quantity < 1:
                return apology("Cannot sell negative stocks")

    symbol = symbol.upper()
    amt = db.execute("SELECT amount FROM stocks WHERE user_id=? AND symbol=?", session['user_id'], symbol)
    dct = amt[0]
    amt = dct['amount']

    if quantity > amt:
        return apology("Insufficient stocks to sell")

    amt -= quantity
    db.execute("UPDATE stocks SET amount = ? WHERE user_id = ? AND symbol = ?", amt, session['user_id'], symbol)

    cash = db.execute("SELECT cash FROM users WHERE id=?", session['user_id'])
    dct = cash[0]
    bal = dct['cash']
    look = lookup(symbol)
    add = quantity * look['price']
    bal += add
    db.execute("UPDATE users SET cash = ? WHERE id = ?", bal, session['user_id'])

    return redirect("/")
