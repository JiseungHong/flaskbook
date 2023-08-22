from flask import Flask, render_template, url_for, request, redirect

app = Flask(__name__)

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

# with app.test_request_context():
#     print(url_for("IDK", name="Love"))
#     print(url_for("show_name", name="Jack"))
    
# Basic Form (PRG)
@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        # TODO: Shoot an E-mail.
        
        # Redirect to "contact_complete" endpoint.
        return redirect(url_for(contact_complete))
    return render_template("contact_complete.html")


if __name__ == '__main__':
    app.run(debug=True)