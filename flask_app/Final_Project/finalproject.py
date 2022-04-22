from flask import Flask, request, redirect, url_for, render_template
import sqlite3 as sql
app = Flask(__name__)

@app.route("/")
def start():
        return render_template("home.htm")

@app.route("/home")
def home():
    return render_template("home.htm")

@app.route("/login", methods = ["POST","GET"])
def main():
    if request.method == "POST":
        username = request.form["un"]
        password = request.form["pw"]
        if password == "Panther$":
            return render_template("home.htm")
        else:
            return render_template("loginf.htm")
    return render_template("loginf.htm")

@app.route("/signup")
def NewUser():
    return render_template("user_info.htm")

@app.route("/dataEntry")
def entry():
    return render_template("product_info.htm")

@app.route("/addEntry/", methods = ["POST", "GET"])
def addEntry():
    if request.method == "POST":
        username = request.form["un"]
        password = request.form["pw"]
        email = request.form["em"]

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Accounts (username, password, email) VALUES ('{0}','{1}','{2}')".format(username, password, email))
        con.commit()

    return render_template("home.htm")

@app.route("/addProduct/", methods = ["POST", "GET"])
def addProduct():
    if request.method == "POST":
        product = request.form["product"]
        description = request.form["description"]
        quantity = request.form["quantity"]
        checkin = request.form["checkin"]

    with sql.connect("database.db") as con:
        cur = con.cursor()
        cur.execute("INSERT INTO Product_Entry (product, description, quantity, checkin) VALUES ('{0}','{1}','{2}','{3}')".format(product, description, quantity, checkin))
        con.commit()

    return render_template("home.htm")


@app.route("/user_list/")
def list():
    con = sql.connect("database.db")
    con.row_factory= sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Accounts")

    rows = cur.fetchall()
    return render_template("user_list.htm", rows = rows)

@app.route("/summary")
def listproduct():
    con = sql.connect("database.db")
    con.row_factory= sql.Row

    cur = con.cursor()
    cur.execute("SELECT * FROM Product_Entry")

    rows = cur.fetchall()
    return render_template("product_list.htm", rows = rows)




if __name__ == "__main__":
    app.run(debug=True)