from email_validator import validate_email, EmailNotValidError
from flask import (Flask, render_template, url_for, request, redirect, 
                   flash,)

app = Flask(__name__)

# For the sake of session security, we assign SECRET_KEY with a random string.
app.config["SECRET_KEY"] = "2AZSMSfnbd6y3hei8"

# Set log level with DEBUG (The lowest)
app.logger.setLevel(logging.DEBUG)

@app.route("/")
def index():
    return "Hello"

# Flask Basics
@app.route("/hello/<name>",
           methods=['GET', 'POST'],
           endpoint='IDK')
def hello(name):
    return f"Hello, {name}!"

@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)

with app.test_request_context():
    print(url_for("IDK", name="Love"))
    print(url_for("show_name", name="Jack"))
    
# Basic Form (PRG)
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # Receive values using 'request.form'.
        username = request.form["username"]
        email = request.form["email"]
        description = request.form["description"]
        
        # Validate values.
        is_valid = True
        if not username:
            flash("Username is null")
            is_valid = False
        
        if not email:
            flash("Email is null")
            is_valid = False
        
        try:
            validate_email(email)
        except EmailNotValidError:
            flash("Email is not valid")
            is_valid = False
        
        if not is_valid:
            return redirect(url_for("contact"))
        
        # TODO: Shoot an E-mail.
        
        
        # Redirect to "contact_complete" endpoint.
        flash("Thank You.")
        return redirect(url_for("contact_complete"))
    return render_template("contact_complete.html")


if __name__ == '__main__':
    app.run(debug=True)