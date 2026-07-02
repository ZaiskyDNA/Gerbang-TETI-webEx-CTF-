import os
import time
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", os.urandom(32))


def load_flag():
    flag = os.environ.get("FLAG")
    if flag:
        return flag

    if os.path.exists("flag.txt"):
        try:
            with open("flag.txt", "r") as f:
                return f.read().strip()
        except Exception:
            pass

    return "NCSC26{dummy_flag_for_development}"


def load_valid_credentials():
    username = os.environ.get("ADMIN_USERNAME")
    password = os.environ.get("ADMIN_PASSWORD")
    if username and password:
        return username, password

    if os.path.exists("admin_creds.txt"):
        try:
            with open("admin_creds.txt", "r") as f:
                content = f.read().strip()
                if "," in content:
                    return content.split(",", 1)
        except Exception:
            pass

    if os.path.exists("credentials.txt"):
        try:
            with open("credentials.txt", "r") as f:
                lines = f.read().splitlines()

            idx_str = os.environ.get("CRED_INDEX")
            if idx_str and idx_str.isdigit():
                idx = int(idx_str)
                if idx < len(lines):
                    return lines[idx].split(",", 1)
        except Exception:
            pass

    return "admin", "admin123"


VALID_USER, VALID_PASSWORD = load_valid_credentials()


@app.route("/")
def index():
    csrf_token = os.urandom(16).hex()
    session['csrf_token'] = csrf_token
    return render_template("login.html", csrf_token=csrf_token)


@app.route("/login", methods=["POST"])
def login():
    csrf_token = request.form.get("csrf_token")
    stored_csrf = session.pop('csrf_token', None) 

    if not stored_csrf or csrf_token != stored_csrf:
        return render_template("error.html", 
                               error_title="CSRF Token Invalid or Missing", 
                               error_desc="Token CSRF Anda tidak valid atau telah kedaluwarsa. Silakan muat ulang halaman login.")

    time.sleep(0.2)

    username = request.form.get("username")
    password = request.form.get("password")

    if username == VALID_USER and password == VALID_PASSWORD:
        current_flag = load_flag()
        return render_template("success.html", flag=current_flag)

    return render_template("error.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)