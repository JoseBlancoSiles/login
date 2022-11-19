# RESUME
Register and Login webapp using Flask/SQL for the backend and HTML/CSS for the frontend. I called this project REGILOG.

![image](https://user-images.githubusercontent.com/107679686/202873412-c4de459a-02a7-4b53-85af-e43596c23f5b.png)

# REGISTER

Register has 3 user-box: username (must be unique), email and password. If the username is not in the BBDD users.db, it appends the user information to the DDBB.
The system automatically sends a message to the user's email to confirm the registration.

# LOGIN
Login has 2 user-box, username and password. If username & password are found in the BBDD you will be logged in the webapp.

# USERS 
in /users you can see all the registrants structed in a table.
The database administrator can delete users from the BBDD by clicking "Deregister". An email is automatically sent to the user.

# HOW TO USE
Take in consideration that you will need to configure the mail like this:

# Configuration to send mail after registration/deregistration
app.config["MAIL_DEFAULT_SENDER"] = myEnval.MAIL_DEFAULT_SENDER
app.config["MAIL_PASSWORD"] = myEnval.MAIL_PASSWORD
app.config["MAIL_PORT"] = 587
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = myEnval.MAIL_USERNAME
mail = Mail(app)

I suggest to create a new folder inside your project called myEnval.py where you can safely storage your passwords and email.

Tu run this webapp code this in your bash terminal:

$ flask run

If any errors ocurs with the application, please don't hesitate writing me on GitHub or LinkedIn.
Thanks!
