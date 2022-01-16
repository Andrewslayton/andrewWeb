from flask import Flask, render_template, request, redirect, url_for, flash


app = Flask(__name__)


@app.route("/")
def index(): 
    return render_template("index.html", )

@app.route("/plans")
def plans():
    return "My plan is to be able to take a google sheets page that is public and calculate multiple categories of lifts off it with built in hyperlink buttons"

@app.route("/1")
def user2():
        return "what lift would you like to calculate"
@app.route("/2")
def supps():
        return render_template("mysupplements.html")

@app.route("/3")
def workoutPlan():
        return render_template("workoutplans.html")
    

@app.route("/login", methods=["POST","GET"]) 
def login():
    if request.method == "POST" :
        user = request.form["nm"]
        if user == "lauren":
            return render_template("lauren.html")
        elif user == "alan":
            return render_template("alanb43.html")
        else:
            return redirect(url_for("user", usr = user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    if usr == alan:
        return render_template("alanb43.html")
    else:
        return f"<h1>{usr}<h1>"

@app.route("/alan#")
def alan():
    return render_template("alanb43.html")


        






if __name__ == "__main__":
    app.run(debug=True)
