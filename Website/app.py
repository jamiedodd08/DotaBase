from multiprocessing import connection
from flask import Flask, render_template,request,redirect,url_for,session,g,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ihoihwfojfweijwf'

mysql = MySQL(app)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "DotaBaseDB"

def addcounterto(cur):
    counterinfo = request.form
    name = counterinfo['countertoname']
    info = counterinfo['countertoinfo']
    cur.execute("INSERT INTO CountersTo(HeroID, CounterUserInfo) VALUES(%s, %s)",(name, info))
    mysql.connection.commit()

def addcounteredby(cur):
    counterinfo = request.form
    name = counterinfo['counteredbyname']
    info = counterinfo['counteredbyinfo']
    cur.execute("INSERT INTO CounteredBy(HeroID, CounteredUserInfo) VALUES(%s, %s)",(name, info))
    mysql.connection.commit()     

def upvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    counterid = uservote['counterid']

    cur.execute('SELECT upvote, downvote FROM CounterToVote WHERE CounterID = %s AND UserID = %s',(counterid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO CounterToVote(UserID, CounterID, upvote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CountersTo SET CounterUpVote = CounterUpVote + 1 WHERE CounterID = %s",(counterid))
        mysql.connection.commit()
        return redirect(request.url)
    
    if a[1] == 1:
        cur.execute("DELETE FROM CounterToVote WHERE CounterID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CountersTo SET CounterDownVote = CounterDownVote - 1 WHERE CounterID = %s",(counterid))
        cur.execute("INSERT INTO CounterToVote(UserID, CounterID, upvote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CountersTo SET CounterUpVote = CounterUpVote + 1 WHERE CounterID = %s",(counterid))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM CounterToVote WHERE CounterID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CountersTo SET CounterUpVote = CounterUpVote - 1 WHERE CounterID = %s",(counterid))
        mysql.connection.commit()

def downvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    counterid = uservote['counterid']

    cur.execute('SELECT upvote, downvote FROM CounterToVote WHERE CounterID = %s AND UserID = %s',(counterid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO CounterToVote(UserID, CounterID, downvote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CountersTo SET CounterDownVote = CounterDownVote + 1 WHERE CounterID = %s",(counterid))
        mysql.connection.commit()
        return redirect(request.url)

    if a[0] == 1:
        cur.execute("DELETE FROM CounterToVote WHERE CounterID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CountersTo SET CounterUpVote = CounterUpVote - 1 WHERE CounterID = %s",(counterid))
        cur.execute("INSERT INTO CounterToVote(UserID, CounterID, downvote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CountersTo SET CounterDownVote = CounterDownVote + 1 WHERE CounterID = %s",(counterid))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM CounterToVote WHERE CounterID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CountersTo SET CounterDownVote = CounterDownVote - 1 WHERE CounterID = %s",(counterid))
        mysql.connection.commit()
    
def gettotalvotes(cur):
    cur.execute("SELECT CounterToTotalVotes, CounterID FROM CountersTo")
    votes = cur.fetchall()
    return votes


@app.before_request
def before_request():
    g.user = None
    if 'id' in session:
        user = session['id']
        g.user = user

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE username =%s AND UserPassword = %s', (username, password,))
        account = cursor.fetchone()
        if account:
            session['loggedin'] = True
            session['id'] = account['UserID']
            session['username'] = account['Username']
            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password, Please try again.'
    return render_template('login.html', msg=msg)

@app.route('/logout')
def logout():
    session.pop('loggedin', None)
    session.pop('id', None)
    session.pop('username', None)
    return redirect(url_for('home'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM Users WHERE Username = %s', (username,))
        account = cursor.fetchone()
        if account:
            msg = 'This account already exists.'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address, Please try again.'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers.'
        elif not username or not password or not email:
            msg = 'Please fill every field.'
        else:
            cursor.execute('INSERT INTO Users VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered.'
    elif request.method == 'POST':
        msg = 'Please fill out form'
    return render_template('register.html',msg=msg)

@app.route('/')
def blank():
    return redirect(url_for('home'))

@app.route('/home')
def home():
    return render_template("home.html",name=g.user)
    
@app.route('/heroes')
def heroes():
    return render_template("heroPool.html")

@app.route('/abaddon', methods=['GET', 'POST'])
def abaddon():
    hname = "Abaddon"
    himg = "static/images/heroes/abaddon.png"
    cur = mysql.connection.cursor()
    cur.execute("SELECT HeroID,HeroName FROM Heroes")
    fetchnames = cur.fetchall()
    cur.execute("SELECT Heroes.HeroIconLink, CountersTo.CounterUserInfo, Heroes.HeroName, CountersTo.CounterID FROM Heroes INNER JOIN CountersTo ON CountersTo.HeroID=Heroes.HeroID")
    fetchcounterto = cur.fetchall()
    cur.execute("SELECT Heroes.HeroIconLink, CounteredBy.CounteredUserInfo, Heroes.HeroName FROM Heroes INNER JOIN CounteredBy ON CounteredBy.HeroID=Heroes.HeroID")
    fetchcounteredby = cur.fetchall()

    t = gettotalvotes(cur)

    if "countertosubmit" in request.form:
        addcounterto(cur)
        return redirect(request.url)
    if "counteredbysubmit" in request.form:
        addcounteredby(cur)
        return redirect(request.url)
    if "upvote" in request.form:
        upvote(cur)
        return redirect(request.url)
    if "downvote" in request.form:
        downvote(cur)
        return redirect(request.url)   

    return render_template("hero.html", heroname=hname, heroimg=himg, heronames=fetchnames, countertoinfo=fetchcounterto, counteredbyinfo=fetchcounteredby, t=t)

@app.route('/alchemist')
def alchemist():
    hname = "Alchemist"
    himg = "static/images/heroes/alchemist.png"
    return render_template("hero.html", heroname=hname, heroimg=himg)

@app.route('/ancient-apparition')
def ancient_apparition():
    hname = "Ancient Apparition"
    himg = "static/images/heroes/ancient_apparition.png"
    return render_template("hero.html", heroname=hname, heroimg=himg)

if __name__ == '__main__':
    app.run(debug=True)
