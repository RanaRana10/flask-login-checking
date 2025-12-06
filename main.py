from flask import Flask, render_template, render_template_string, redirect, flash
from forms import LoginForm

app = Flask(
    __name__,
    template_folder="templates",  # replace templates
    static_folder="static",  # replace static
)

app.secret_key = "your-secret-key"  # Required for CSRF


@app.route("/")
def hello_world():
    return render_template_string("<h1>index.html is this page</h1>")


@app.route("/l", methods=["GET", "POST"])
@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():  # type: ignore
        email = form.email.data
        password = form.password.data

        # Example check
        if email == "test@example.com" and password == "1234":
            flash("Login successful!")  # Will show on next page
            return redirect("/dashboard")

        elif email == "a@b.c" and password == "a":
            flash("Login successful!")  # Will show on next page
            return redirect("/dashboard")

        else:
            flash("Invalid email or password!")  # Will show on login page
            return render_template("login.html", form=form)
    flash("Some Data not validate till now")  # when email maybe not validate
    return render_template("login.html", form=form)


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000,
    )
