import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

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

    overview = db.execute(
        """SELECT stocks.symbol, stocks.company, stocks.shares,
    users.cash FROM stocks JOIN users ON stocks.user_id = users.id
    WHERE users.id = ?""",
        session["user_id"],
    )

    if len(overview) != 0:
        total = overview[0]["cash"]

        for i in range(len(overview)):
            overview[i]["current_price"] = lookup(overview[i]["symbol"])["price"]
            overview[i]["value"] = overview[i]["current_price"] * overview[i]["shares"]
            total += overview[i]["value"]

        return render_template(
            "index.html", overview=overview, cash=overview[0]["cash"], total=total
        )

    # showing only available cash if no Stocks are owned
    cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
    return render_template("index.html", cash=cash[0]["cash"])


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        # Validate Inputs
        if lookup(request.form.get("symbol")) != None:
            stock = lookup(request.form.get("symbol"))
        else:
            return apology("Invalid Stock Symbol", 400)

        if (
            not request.form.get("shares").isdigit()
            or request.form.get("shares") == "0"
        ):
            return apology("Please Enter A Valid Amount")

        shares = int(request.form.get("shares"))
        total = stock["price"] * shares
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session["user_id"])
        new_amount = cash[0]["cash"] - total

        # validate Funds
        if new_amount < 0:
            return apology("Insufficiant Funds", 400)

        # creating Tables to track owened stocks and transaction History
        db.execute(
            """CREATE TABLE IF NOT EXISTS stocks (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   user_id NUMERIC NOT NULL, company TEXT NOT NULL, symbol TEXT NOT NULL,
                   shares NUMERIC NOT NULL, FOREIGN KEY (user_id) REFERENCES users(id))"""
        )

        db.execute(
            """CREATE TABLE IF NOT EXISTS history (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                   user_id NUMERIC NOT NULL, type TEXT NOT NULL, symbol TEXT NOT NULL, stock_price NUMERIC NOT NULL,
                   timestamp DATETIME DEFAULT CURRENT_TIMESTAMP, shares NUMERIC NOT NULL,
                   FOREIGN KEY (user_id) REFERENCES users(id))"""
        )

        # track transaction History and update owend cash
        db.execute(
            "INSERT INTO history (user_id, type, symbol, stock_price, shares) VALUES (?,?,?,?,?)",
            session["user_id"],
            "acquisition",
            stock["symbol"],
            stock["price"],
            shares,
        )
        db.execute(
            "UPDATE users SET cash = ? WHERE id = ?", new_amount, session["user_id"]
        )

        # Update owed stocks depending on Stocks already owned
        already_stocks = db.execute(
            "SELECT * FROM stocks WHERE user_id = ? AND symbol = ?",
            session["user_id"],
            stock["symbol"],
        )
        if already_stocks:
            db.execute(
                "UPDATE stocks SET shares = (shares + ?) WHERE user_id = ? AND symbol = ?",
                shares,
                session["user_id"],
                stock["symbol"],
            )
        else:
            db.execute(
                "INSERT INTO stocks (user_id, company, symbol, shares) VALUES (?,?,?,?)",
                session["user_id"],
                stock["name"],
                stock["symbol"],
                shares,
            )

        return redirect("/")

    return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """display Overview of Transactions"""
    history = db.execute("SELECT * FROM history WHERE user_id = ?", session["user_id"])
    return render_template("history.html", history=history)


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
    if request.method == "POST":
        # Validate inputs
        if lookup(request.form.get("symbol")) == None:
            return apology("Invalid Stock Symbol", 400)

        price = lookup(request.form.get("symbol"))
        return render_template("quoted.html", name=price["name"], price=price["price"])

    return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    # creating a list of all usernasmes in db to avoid duplicates
    username_list = []
    usernames = db.execute("SELECT username from users;")
    for name in usernames:
        username_list.append(name["username"])

    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        elif request.form.get("username") in username_list:
            return apology("Username already in use", 400)

        # Ensure password was submitted correctly
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords not equal", 400)

        username = request.form.get("username")
        password = generate_password_hash(request.form.get("password"))

        db.execute(
            "INSERT INTO users (username, hash) VALUES (?,?)", username, password
        )
        return redirect("/login")

    return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    if request.method == "POST":
        # Validate inputs
        if lookup(request.form.get("symbol")) == None:
            return apology("Invalid Stock Symbol", 400)

        elif (
            not request.form.get("shares").isdigit()
            or request.form.get("shares") == "0"
        ):
            return apology("Please Enter The Amount of Shares To Sell")

        shares = int(request.form.get("shares"))
        stock = lookup(request.form.get("symbol"))

        symbols = db.execute(
            "SELECT symbol FROM stocks Where user_id = ?", session["user_id"]
        )
        # ensures that the User owns stock of type symbol
        for i in range(len(symbols)):
            if request.form.get("symbol") in symbols[i].values():
                break
        else:
            return apology("You Do Not Own Shares from this Company", 400)

        # ensures that the User has enough shares
        shares = db.execute(
            "SELECT shares FROM stocks Where user_id = ? AND symbol = ?",
            session["user_id"],
            request.form.get("symbol"),
        )
        if int(request.form.get("shares")) > shares[0]["shares"]:
            return apology("You Do Not Have This Many Shares", 400)

        # Updates transaction history
        db.execute(
            "INSERT INTO history (user_id, type, symbol, stock_price, shares) VALUES (?,?,?,?,?)",
            session["user_id"],
            "Divestiture",
            stock["symbol"],
            stock["price"],
            shares[0]["shares"],
        )

        # updates the portfolio and clears entries with 0 shares
        db.execute(
            "UPDATE stocks SET shares = (shares - ?) WHERE user_id = ? AND symbol = ?",
            request.form.get("shares"),
            session["user_id"],
            request.form.get("symbol"),
        )
        db.execute("DELETE FROM stocks WHERE shares = 0")

        return redirect("/")

    # enures the List of available symbols is shown right away
    symbols = db.execute(
        "SELECT symbol FROM stocks Where user_id = ?", session["user_id"]
    )
    return render_template("sell.html", symbols=symbols)


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """Allows to Deposit Cash into Account"""
    if request.method == "POST":
        # validates Inputs
        try:
            if int(request.form["deposit"]) < 0:
                return apology("Invalid Amount", 400)

        except ValueError:
            return apology("Invalid Input", 400)

        # updates the users table with new cash amount
        db.execute(
            "UPDATE users SET cash = cash + ? WHERE id = ?",
            request.form["deposit"],
            session["user_id"],
        )

        # updates the history table
        db.execute(
            "INSERT INTO history (user_id, type, symbol, stock_price, shares) VALUES (?,?,?,?,?)",
            session["user_id"],
            "Deposit",
            "",
            request.form["deposit"],
            "",
        )

        return redirect("/")

    return render_template("deposit.html")
