from flask import Blueprint, render_template, request, redirect
from database import conn, cursor

register_bp = Blueprint("register", __name__)


@register_bp.route("/registration", methods=["GET", "POST"])
def registration():

    if request.method == "POST":

        username = request.form["username"]
        password = request.form["password"]

        try:

            query = """
            INSERT INTO users(username,password)
            VALUES(%s,%s)
            """

            cursor.execute(query, (username, password))
            conn.commit()

            return redirect("/login")

        except Exception as e:
            return f"Error : {e}"

    return render_template("registration.html")