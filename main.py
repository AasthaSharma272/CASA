import time

import emotions
from piece_producing import produce_piece 

from flask import flash, Flask, render_template, redirect, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required

# database
from replit import db

app = Flask(__name__)

# auto-reload templates
app.config["TEMPLATES_AUTO_RELOAD"] = True

# ensure responses are not cached (after logout)
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


@app.route('/', methods=["GET", "POST"])
@login_required
def index():
  if request.method == "POST":
    #GLOBAL VARIABLES RAAAH
    global FEEL
    global FORMAT
    global DATE
    global PARA1
    global FILE
    
    FEEL = request.form.get("feel")
    print(FEEL)
    FORMAT = request.form.get("format")
    print(FORMAT)
    lang = request.form.get("lang")
    if not lang:
      lang = "english"
      
    DATE = time.ctime()

    # produces string with file
    PARA1 = str(emotions.final(FEEL))
    print(PARA1)
    FILE = produce_piece(PARA1, str(FORMAT),str(lang))
    
    return render_template("results.html", format=FORMAT, file=FILE)
  else:
    return render_template("index.html")


@app.route('/history')
@login_required
def history():
  return render_template("history.html", date=DATE, format=FORMAT, file=FILE, feel=FEEL, para=PARA1)


@app.route('/login', methods=["GET", "POST"])
def login():
  # clear previous session
  session.clear()

  if request.method == "POST":
    username = request.form.get("username")
    password = request.form.get("password")

    # check for blanks
    if not username:
      print("username error")
      return apology("Please enter your username", "login.html")
    elif not password:
      print("password error")
      return apology("Please enter your password", "login.html")

    # check if username exists
    pass_hash = db[username]
    if not pass_hash or not check_password_hash(pass_hash, password):
      print("wonkydoodle")
      return apology("Invalid username or password, please try again", "login.html")

    # remember user
    session["user_id"] = username
    return redirect("/")
    
  else:
    return render_template("login.html")

@app.route('/logout')
def logout():
  session.clear()

  # flash a comment
  
  return redirect('/')

@app.route('/register', methods=["GET", "POST"])
def register():
  if request.method == "POST":
    print("post success")
    username = request.form.get("username")
    print(username)
    password = request.form.get("password")
    print(password)

    # check for blank values
    if not username:
      print("username error")
      return apology("Please enter your username", "register.html")
    elif not password:
      print("password error")
      return apology("Please enter your password", "register.html")
    elif password != request.form.get("confirm"):
      print("no match")
      return apology("Your username and password do not match, please try again", "register.html")

    # all values should be full, check if username is valid
    else:
      # look for username
      if username in db:
        flash(f"Someone else has the username { username }, whoops!")
        return apology(f"The username { username } is already in use.", "register.html")
      
      pass_hash = generate_password_hash(password) 

      # adds username and password to db
      db[username] = pass_hash
      print(db[username])
      return redirect("/login")

  
  else:
    print("get")
    return render_template("register.html")


app.run(host='0.0.0.0', port=81)

