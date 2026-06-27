from flask import Flask, redirect

app = Flask(__name__)

# Register blueprints
from login import login_bp
from register import register_bp

app.register_blueprint(login_bp)
app.register_blueprint(register_bp)


@app.route("/")
def home():
    return redirect("/login")


if __name__ == "__main__":
    app.run(debug=True)