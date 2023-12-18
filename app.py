from flask import Flask
from flask import Flask, redirect, render_template, request, session
from cs50 import SQL
from datetime import date
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from tempfile import mkdtemp
from helpers import apology, login_required
from calc_price import price
from sql import init_db


app = Flask(__name__)
db = SQL("sqlite:///database.db")

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)
init_db()  # used when first time app created to define and insert values into a table

user = {
    'is_authenticated' : False,
}

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

    travel_details = db.execute("SELECT * FROM travels WHERE user_id = ?", user_id)
    try:
        src = travel_details[-1]["source"]
        dest = travel_details[-1]["dest"]
        amount = travel_details[-1]["amount"]
        date = travel_details[-1]["date"]
    except:
        src = "None"
        dest = "None"
        amount = "None"
        date = "None"

    last_ride = src + " - " + dest
    
    pass_type = db.execute("SELECT pass_type FROM user_pass WHERE user_id = ?", user_id)[0]["pass_type"]

    return render_template(
        "profile.html",
        name=name,
        age=age,
        gender=gender,
        credits=credits,
        last_ride=last_ride,
        amount=amount,
        date=date,
        pass_type=pass_type,
    )


@app.route("/register", methods=["GET", "POST"])
def register():
    session.clear()

    if request.method == "POST":
        # ensure username was submitted
        if not request.form.get("username"):
            return apology(message="must provide username", code=403)

        # ensure password was submitted
        elif not request.form.get("password"):
            return apology(message="must provide password", code=403)

        # ensure passwords match
        elif request.form.get("password") != request.form.get("confirmation"):
            return apology(message="passwords do not match", code=403)

        # save username and password hash in variables
        username = request.form.get("username")
        password = request.form.get("password")
        hashed_password = generate_password_hash(password)

        # Insert into user_auth first
        result = db.execute("INSERT INTO user_auth (hash) VALUES (?)", hashed_password)
        user_id = result

        # Query database to ensure username isn't already taken
        rows = db.execute("SELECT * FROM users WHERE name = ?", username)
        if len(rows) != 0:
            return apology(message="username is already taken", code=403)

        age = request.form.get("age")
        gender = request.form.get("gender")

        # insert into users using the obtained user_id
        db.execute(
            "INSERT INTO users (user_id, name, age, gender) VALUES (?, ?, ?, ?)",
            user_id,
            username,
            age,
            gender,
        )
        db.execute("INSERT INTO user_pass (user_id, pass_type) VALUES (?, ?)", user_id, "No pass")

        # redirect to login page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html", )



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology(message="must provide username", code=403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology(message="must provide password", code=403)

        # Query database for username
        try:
            user_id_q = db.execute(
                "SELECT user_id FROM users WHERE name = ?", request.form.get("username")
            )[0]["user_id"]
        except IndexError:
            return apology(message="Register first", code=403)

            
        pw_hash = db.execute("SELECT hash from user_auth WHERE user_id = ?", user_id_q)[
            0
        ]["hash"]

        # Ensure username exists and password is correct
        if not user_id_q or not check_password_hash(
            pw_hash, request.form.get("password")
        ):
            return apology(message="invalid username and/or password", code=403)

        # Remember which user has logged in
        session["user_id"] = user_id_q

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html", )


@app.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    session.clear()
    return redirect("/")

@app.route("/pass", methods=["GET", "POST"])
@login_required
def buy_pass():
    if request.method == "POST":
        user_id = session["user_id"]
        
        has_pass = db.execute("SELECT pass_type FROM user_pass where user_id = ?", user_id)[0][
            "pass_type"
        ]
        if has_pass == "general" or has_pass == "executive":
            return apology(message="You already have a pass", code=403)
        
        amount = 0
        pass_type = request.form.get("pass")
        if pass_type == "general":
            amount = 100
        elif pass_type == "executive":
            amount = 300

        cash = db.execute("SELECT credits FROM users where user_id = ?", user_id)[0][
            "credits"
        ]
        
        if cash < amount:
            return apology(message="Insufficient funds", code=403)
        else:
            rem = cash - amount
            # db.execute("CALL DeductCredits(?, ?)", user_id, amount)
            db.execute("UPDATE users SET credits = ? WHERE user_id = ?", rem, user_id)
            db.execute("UPDATE user_pass SET pass_type = ? WHERE user_id = ?", pass_type, user_id)
        
        return redirect("/profile")
    
    else:
        return render_template("pass.html")


@app.route("/book", methods=["GET", "POST"])
@login_required
def buy_ticket():
    # q = ['Challaghatta', 'Kengeri Bus Terminal','Mailasandra','Pattanagere', 'Jnanabharathi', 'Rajarajeshwari Nagar', 'Nayandahalli','Mysuru Road',
    # 'Deepanjali Nagar','Deepanjali Nagar', 'Attiguppe','Vijayanagar', 'BGS Hosahalli','Magadi Road','KSR City Railway Station', 'Nadaprabhu Kempe Gowda Majestic',
    # 'Sir M Visveswaraya Central College','Dr. B R Ambedkar Vidhana Soudha', 'Cubbon Park','Mahatma Gandhi Road','Trinity', 'Halasuru','Indiranagar', 'Swami Vivekananda Road',
    # 'Baiyyappanahalli','Benniganahalli','Mahadevpura', 'Garudacharpalya','Hoodi Junction','Sitarama Palya','Kundalahalli','Nallurahalli', 'Sadaramangala','Pattanduru Agrahara'
    # ,'Kadugodi Industrial Area', 'Channasandra', 'Whitefield','Madavara', 'Chikkabidirakallu', 'Manjunath Nagar', 'Nagasandra', 'Dasarahalli', 'Jalahalli', 'Peenya Industry',
    # 'Peenya', 'Goraguntepalya', 'Yeshwantpur', 'Sandal Soap Factory', 'MAhalaxmi', 'Rajajinagar', 'Kuvempu Road', 'Srirampura', 'Mantri Square Sampige Road', 'Chickpete',
    # 'Krishna Rajendra Market', 'National College', 'Lalbagh', 'South End Circle', 'Jayanagar', 'Rashtriya Vidhyalaya Road', 'Banashankari', 'Jayaprakash NAgar',
    # 'Yelachenahalli', 'Konanakunte Cross', 'Doddakallasandra','Vajrahalli','Thalaghattapura', 'Anjanapura']

    q = db.execute("SELECT stn_name FROM stations")
    stations = []
    for stn in q:
        stations.append(stn["stn_name"])

    if request.method == "POST":
        # Ensure username was submitted
        source = request.form.get("source")
        if not source:
            return apology(message="must provide source station", code=403)

        # Ensure password was submitted
        destination = request.form.get("destination")
        if not destination:
            return apology(message="must provide destination station", code=403)

        user_id = session["user_id"]
        pass_type = db.execute("SELECT pass_type FROM user_pass where user_id = ?", user_id)[0][
            "pass_type"
        ]

        fare = price(source, destination, pass_type)

        cash = db.execute("SELECT credits FROM users where user_id = ?", user_id)[0][
            "credits"
        ]

        today = date.today()
        remainder = cash - fare
        if remainder < 0:
            return apology(message="Insufficient funds", code=403)

        db.execute(
            "INSERT INTO travels (user_id, source, dest, amount, date) VALUES(?, ?, ?, ?, ?)",
            user_id,
            source,
            destination,
            fare,
            today,
        )
        
        # db.execute("CALL DeductCredits(?, ?)", user_id, fare)
        # db.execute("UPDATE users SET credits = ? WHERE user_id = ?", remainder, user_id)

        return render_template("tickets.html", price=fare)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("tickets.html", q=stations)


@app.route("/about")
def about():
    return render_template("about.html", )


# /history route
@app.route("/history")
@login_required
def history():
    user_id = session["user_id"]

    # Include travel_id in the query
    travels = db.execute("SELECT travel_id, source, dest, amount, date FROM travels WHERE user_id = ?", user_id)

    cash = db.execute("SELECT credits FROM users WHERE user_id = ?", user_id)[0]["credits"]
    print(travels)
    return render_template("history.html", travels=travels, cash=cash)


# /wallet route
@app.route("/wallet", methods=["GET", "POST"])
@login_required
def wallet():
    user_id = session["user_id"]

    # Include travel_id in the query
    travels = db.execute("SELECT travel_id, date, amount, date FROM travels WHERE user_id = ?", user_id)

    cash = db.execute("SELECT credits FROM users WHERE user_id = ?", user_id)[0]["credits"]
    pass_type = db.execute("SELECT pass_type FROM user_pass WHERE user_id = ?", user_id)[0]["pass_type"]

    print(travels)
    return render_template("wallet.html", travels=travels, cash=cash, pass_type=pass_type)



@app.route("/map")
def map():
    return render_template("map.html")


if __name__ == "__main__":
    app.run(debug=True)
