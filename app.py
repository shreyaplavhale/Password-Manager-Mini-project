from flask import Flask, render_template, request, redirect

import pymysql

from cryptography.fernet import Fernet


# Load Secret Key
with open("secret.key", "rb") as file:
    key = file.read()

fernet = Fernet(key)


app = Flask(__name__)


# MySQL Connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="RS12@shrey",
    database="password_manager"
)

cursor = connection.cursor()


# Home Page
@app.route("/")
def home():

    sql = "SELECT * FROM password"

    cursor.execute(sql)

    passwords = cursor.fetchall()

    decrypted_passwords = []

    for item in passwords:

        decrypted = (
            fernet.decrypt(
                item[3].encode()
            ).decode()
        )

        decrypted_passwords.append(
            (
                item[0],
                item[1],
                item[2],
                decrypted
            )
        )

    return render_template(
        "index.html",
        passwords=decrypted_passwords
    )


# Save Password
@app.route("/save", methods=["POST"])
def save_password():

    website = request.form["website"]

    username = request.form["username"]

    password = request.form["password"]

    # Encrypt Password
    encrypted_password = (
        fernet.encrypt(
            password.encode()
        ).decode()
    )

    sql = """
    INSERT INTO password
    (website, username, password)
    VALUES (%s, %s, %s)
    """

    values = (
        website,
        username,
        encrypted_password
    )

    cursor.execute(sql, values)

    connection.commit()

    return redirect("/")


# Delete Password
@app.route("/delete/<int:id>")
def delete_password(id):

    sql = "DELETE FROM password WHERE id=%s"

    cursor.execute(sql, (id,))

    connection.commit()

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)