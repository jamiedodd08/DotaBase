from multiprocessing import connection
from flask import Flask, render_template,request
from flask_mysqldb import MySQL

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ihoihwfojfweijwf'

mysql = MySQL(app)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "DotaBaseDB"

@app.route('/home')
def home():
    return render_template("home.html")

@app.route('/heroes')
def heroes():
    return render_template("heroPool.html")

@app.route('/abaddon')
def abaddon():
    hname = "Abaddon"
    himg = "static/images/heroes/abaddon.png"
    return render_template("hero.html", heroname=hname, heroimg=himg)

@app.route('/alchemist')
def alchesmist():
    hname = "Alchemist"
    himg = "static/images/heroes/alchemist.png"
    return render_template("hero.html", heroname=hname, heroimg=himg)

if __name__ == '__main__':
    app.run(debug=True)
