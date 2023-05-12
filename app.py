from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session
from cs50 import SQL
from datetime import date
from flask_session import Session
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp
from helpers import apology, login_required
from flask_qrcode import QRcode
from newalgo import algo


app = Flask(__name__)
db = SQL("sqlite:///database.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def index():
    return render_template("home.html")

@app.route("/profile")
@login_required
def profile():
    user_id = session["user_id"]

    person = db.execute("SELECT * FROM users where user_id = ?", user_id)

    name = person[0]["name"]
    age = person[0]["age"]
    gender = person[0]["gender"]
    credits = person[0]["credits"]


    travel_details = db.execute("SELECT * FROM travels WHERE id = ?", user_id)
    try:
        src = travel_details[0]["source"]
        dest = travel_details[0]["dest"]
        amount = travel_details[0]["amount"]
        date = travel_details[0]["date"]
    except:
         return redirect('/book')
        


    last_ride = (src + " - " + dest)

         

    return render_template("profile.html", name=name, age=age, gender=gender, credits=credits, last_ride=last_ride, amount=amount, date=date)

@app.route("/register", methods=["GET", "POST"])
def register():

    session.clear()

    if request.method == "POST":

        # ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords do not match", 403)

        # save username and password hash in variables
        username = request.form.get("username")
        hash = generate_password_hash(request.form.get("password"))

        # Query database to ensure username isn't already taken
        rows = db.execute("SELECT * FROM users WHERE name = ?", username)
        if len(rows) != 0:
            return apology("username is already taken", 403)

        age = request.form.get("age")
        gender = request.form.get("gender")

        # insert username and hash into database
        db.execute("INSERT INTO users (name, hash, age, gender) VALUES (? ,?, ?, ?)", \
                   username, hash, age, gender)

        # redirect to login page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE name = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["user_id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():

    session.clear()
    return redirect("/")

@app.route("/book", methods=["GET", "POST"])
@login_required
def buy():
    q=['Challaghatta', 'Kengeri Bus Terminal','Mailasandra','Pattanagere', 'Jnanabharathi', 'Rajarajeshwari Nagar', 'Nayandahalli','Mysuru Road',
    'Deepanjali Nagar','Deepanjali Nagar', 'Attiguppe','Vijayanagar', 'BGS Hosahalli','Magadi Road','KSR City Railway Station', 'Nadaprabhu Kempe Gowda Majestic',
    'Sir M Visveswaraya Central College','Dr. B R Ambedkar Vidhana Soudha', 'Cubbon Park','Mahatma Gandhi Road','Trinity', 'Halasuru','Indiranagar', 'Swami Vivekananda Road',
    'Baiyyappanahalli','Benniganahalli','Mahadevpura', 'Garudacharpalya','Hoodi Junction','Sitarama Palya','Kundalahalli','Nallurahalli', 'Sadaramangala','Pattanduru Agrahara'
    ,'Kadugodi Industrial Area', 'Channasandra', 'Whitefield','Madavara', 'Chikkabidirakallu', 'Manjunath Nagar', 'Nagasandra', 'Dasarahalli', 'Jalahalli', 'Peenya Industry',
    'Peenya', 'Goraguntepalya', 'Yeshwantpur', 'Sandal Soap Factory', 'MAhalaxmi', 'Rajajinagar', 'Kuvempu Road', 'Srirampura', 'Mantri Square Sampige Road', 'Chickpete',
    'Krishna Rajendra Market', 'National College', 'Lalbagh', 'South End Circle', 'Jayanagar', 'Rashtriya Vidhyalaya Road', 'Banashankari', 'Jayaprakash NAgar',
    'Yelachenahalli', 'Konanakunte Cross', 'Doddakallasandra','Vajrahalli','Thalaghattapura', 'Anjanapura']
    if request.method == "POST":
        # Ensure username was submitted
        source =  request.form.get("source")
        print(source)
        if not source:
            return apology("must provide source station", 403)

        # Ensure password was submitted
        destination = request.form.get("destination")
        print(destination)
        if not destination:
            return apology("must provide destination station", 403)

        price = int(algo(source,destination))

        user_id = session["user_id"]

        cash = db.execute("SELECT credits FROM users where user_id = ?", user_id)[0]['credits']

        today = date.today()
        remainder = cash - price
        if remainder < 0:
            return apology("insufficient funds", 403)

        db.execute("INSERT INTO travels (id,source,dest,amount,date) VALUES(?,?,?,?,?)",user_id,source,destination,price,today)

        db.execute("UPDATE users SET credits = ? WHERE user_id = ?",remainder,user_id)

        return render_template("tickets.html",price=price)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("tickets.html",q=q)

@app.route("/history")
@login_required
def history():

    user_id = session["user_id"]

    person = db.execute("SELECT * FROM travels WHERE id = ?", user_id)
    cash = db.execute("SELECT credits FROM users WHERE user_id = ?", user_id)[0]["credits"];
    return render_template("history.html", person=person, cash=cash)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/wallet", methods=["GET", "POST"])
@login_required
def wallet():

    user_id = session["user_id"]

    travels = db.execute("SELECT * FROM travels WHERE id = ?", user_id)
    cash = db.execute("SELECT credits FROM users WHERE user_id = ?", user_id)[0]["credits"];

    return render_template("wallet.html", travels=travels, cash=cash)


@app.route("/map")
def map():
    return render_template("map.html")