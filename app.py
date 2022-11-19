# Implements a reigstration form, storing users in a SQLite database, sends email of confirmation register/deregister.


from flask import Flask, redirect, render_template, request, session
from flask_mail import Mail, Message
from flask_session import Session
import sqlite3
import myEnval


app = Flask(__name__)


# Session configuration
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Configuration to send mail after registration/deregistration
app.config["MAIL_DEFAULT_SENDER"] = myEnval.MAIL_DEFAULT_SENDER
app.config["MAIL_PASSWORD"] = myEnval.MAIL_PASSWORD
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = myEnval.MAIL_USERNAME
mail = Mail(app)


SPORTS = [
  "Basketball",
  "Football",
  "Ultimate Frisbee"
]


@app.route('/', methods=["GET","POST"])
def index():
  return render_template("index.html", sports=SPORTS)


@app.route("/register", methods=["POST"])
def register():
  
  # Validate submission
  username = request.form.get("username")
  # if not username:
  #   return render_template("failure.html", message="Missing username")
  
  con = sqlite3.connect('users.db')
  cursor = con.cursor()
      
  query = "SELECT username FROM users WHERE username= '"+username+"'"
  cursor.execute(query)
  
  usernames = cursor.fetchall()
  
  if len(usernames) != 0:
    return render_template("registered.html")    
  
  email = request.form.get("email")
  # if not email:
  #   return render_template("failure.html", message="Missing email")
  
  password = request.form.get('password')
  
  # if not password:
  #   return render_template("failure.html", message="Missing password")
  
  # Remember registrant
  cursor.execute("INSERT INTO users (username, email, password) VALUES(?,?,?)", (username, email, password))
  con.commit()
  
  # Message to the user's gmail to confirm the registration.
  message = Message(body = "You are registered", recipients=[email], subject="Thanks for using REGILOG")
  mail.send(message)
  
  return render_template("success.html")


@app.route("/login", methods=["GET","POST"])
def login():
  
  con = sqlite3.connect('users.db')
  cursor = con.cursor()
  username = request.form.get("username")
  
  cursor.execute("SELECT username FROM users WHERE username =?",(username,))
  usernames = cursor.fetchall()
  print("mail", usernames)
  
  # If list emails is not 0 means that at least 1 email with the same username has been found in the database
  if len(usernames) != 0:
    session['username'] = request.form.get('username')
    
    return render_template("login.html")
  else:
    return render_template("not_registered.html")


@app.route("/logout", methods=["GET","POST"])
def logout():
  session['email'] = None
  return redirect('/')


@app.route("/users")
def users():
  con = sqlite3.connect('users.db')
  # Show all the users
  users = con.execute("SELECT * FROM users")
  con.commit()
  return render_template("users.html", users=users)


@app.route("/deregister", methods=["POST","GET"])
def deregister():
  con = sqlite3.connect('users.db')
  id = request.form.get("id")
  email = request.form.get("email")
  
  # Delete user if exists:
  if id:
    message = Message(recipients=[email], body= "You have been removed", subject="Thanks for using REGILOG") 
    mail.send(message)
    # Remember to use commit so changes will be applied to the database
    con.execute("DELETE FROM users WHERE id=?",(id,))
    con.commit()
  return redirect("/users")