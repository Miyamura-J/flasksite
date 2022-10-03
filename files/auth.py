from flask import Blueprint, render_template, request, flash

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return render_template("login.html")

@auth.route("/logout")
def logout():
    return render_template("home.html")

@auth.route("/sign_up", methods=["GET","POST"])
def sign_up():
    if request.method == "POST":
        email = request.form.get("email")
        fullName = request.form.get("name")
        password1 = request.form.get("password1")
        password2 = request.form.get("password2")
        valid = True
        if len(email) < 4:
            valid = False
            flash("Email must be at least 4 characters", category="error")
        if len(fullName) < 2:
            valid = False
            flash("Name must be at least 2 characters", category="error")
        if password1 != password2:
            valid = False
            flash("Passwords don't match", category="error")
        if len(password1) < 8:
            valid = False
            flash("Password must be at least 8 characters", category="error")
        if valid:
            # add to db
            flash("Account created", category="success")

    return render_template("sign_up.html")
