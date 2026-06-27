from flask import Blueprint, render_template, request
from database import cursor

login_bp = Blueprint("login", __name__)


@login_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        query = """
        SELECT *
        FROM users
        WHERE username=%s
        AND password=%s
        """

        cursor.execute(query, (username, password))

        user = cursor.fetchone()

        if user:

            return f"""
            <h1>Login Successful ✅</h1>
            <h2>Welcome {username}</h2>
            """

        return "<h2>Invalid Username or Password ❌</h2>"

    return render_template("login.html")