from multiprocessing import connection
from flask import Flask, render_template,request,redirect,url_for,session,g,flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re
import string

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ihoihwfojfweijwf'

mysql = MySQL(app)
app.config['MYSQL_HOST'] = "localhost"
app.config['MYSQL_USER'] = "root"
app.config['MYSQL_PASSWORD'] = ""
app.config['MYSQL_DB'] = "DotaBaseDB"


# FUNCTION TO ADD ABILITY INFO
def addabilityinfo(cur):
    user = session['id']
    abilityinfo = request.form
    info = abilityinfo['abilityinfoinput']
    id = abilityinfo['abilityid']
    tag = abilityinfo['abilitytag']
    cur.execute("INSERT INTO AbilityInfo(AbilityID, UserID, AbilityUserInfo, AbilityTag) VALUES(%s, %s, %s, %s)",(id, user, info, tag))
    mysql.connection.commit()

# FUNCTION TO ADD A COUNTER TO HERO PAGE
def addcounterto(cur):
    user = session['id']
    counterinfo = request.form
    name = counterinfo['countertoname']
    info = counterinfo['countertoinfo']
    tag = counterinfo['countertag']
    cur.execute("INSERT INTO CountersTo(HeroID, CounterUserInfo, UserID, CounterTag) VALUES(%s, %s, %s, %s)",(name, info, user, tag))
    mysql.connection.commit()

# FUNCTION TO ADD COUNTERED BY TO HERO PAGE
def addcounteredby(cur):
    user = session['id']
    counterinfo = request.form
    name = counterinfo['counteredbyname']
    info = counterinfo['counteredbyinfo']
    tag = counterinfo['counteredtag']
    cur.execute("INSERT INTO CounteredBy(HeroID, CounteredUserInfo, UserID, CounteredTag) VALUES(%s, %s, %s, %s)",(name, info, user, tag))
    mysql.connection.commit()     

# FUNCTION TO UP VOTE ON THE COUNTER TO SECTION
def countertoupvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    counterid = uservote['counterid']

    cur.execute('SELECT CounterUpVote, CounterDownVote FROM CounterToVote WHERE CounterID = %s AND UserID = %s',(counterid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO CounterToVote(UserID, CounterID, CounterUpVote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CountersTo SET CounterTotalUpVote = CounterTotalUpVote + 1 WHERE CounterID = %s",(counterid,))
        mysql.connection.commit()
        return redirect(request.url)
    
    if a[1] == 1:
        cur.execute("DELETE FROM CounterToVote WHERE CounterID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CountersTo SET CounterTotalDownVote = CounterTotalDownVote - 1 WHERE CounterID = %s",(counterid,))
        cur.execute("INSERT INTO CounterToVote(UserID, CounterID, CounterUpVote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CountersTo SET CounterTotalUpVote = CounterTotalUpVote + 1 WHERE CounterID = %s",(counterid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM CounterToVote WHERE CounterID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CountersTo SET CounterTotalUpVote = CounterTotalUpVote - 1 WHERE CounterID = %s",(counterid,))
        mysql.connection.commit()

# FUNCTION TO DOWN VOTE ON THE COUNTER TO SECTION 
def countertodownvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    counterid = uservote['counterid']

    cur.execute('SELECT CounterUpVote, CounterDownVote FROM CounterToVote WHERE CounterID = %s AND UserID = %s',(counterid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO CounterToVote(UserID, CounterID, CounterDownVote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CountersTo SET CounterTotalDownVote = CounterTotalDownVote + 1 WHERE CounterID = %s",(counterid,))
        mysql.connection.commit()
        return redirect(request.url)

    if a[0] == 1:
        cur.execute("DELETE FROM CounterToVote WHERE CounterID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CountersTo SET CounterTotalUpVote = CounterTotalUpVote - 1 WHERE CounterID = %s",(counterid,))
        cur.execute("INSERT INTO CounterToVote(UserID, CounterID, CounterDownVote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CountersTo SET CounterTotalDownVote = CounterTotalDownVote + 1 WHERE CounterID = %s",(counterid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM CounterToVote WHERE CounterID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CountersTo SET CounterTotalDownVote = CounterTotalDownVote - 1 WHERE CounterID = %s",(counterid,))
        mysql.connection.commit()

# FUNCTION TO RETURN TOTAL VOTES OF EACH COUNTER TO ENTRY 
def countertototalvotes(cur):
    cur.execute("SELECT CounterToTotalVotes, CounterID FROM CountersTo")
    votes = cur.fetchall()
    return votes

# FUNCTION TO UP VOTE ON THE COUNTERED BY SECTION
def counteredbyupvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    counterid = uservote['counterid']

    cur.execute('SELECT CounteredUpVote, CounteredDownVote FROM CounteredByVote WHERE CounteredID = %s AND UserID = %s',(counterid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO CounteredByVote(UserID, CounteredID, CounteredUpVote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CounteredBy SET CounteredTotalUpVote = CounteredTotalUpVote + 1 WHERE CounteredID = %s",(counterid,))
        mysql.connection.commit()
        return redirect(request.url)
    
    if a[1] == 1:
        cur.execute("DELETE FROM CounteredByVote WHERE CounteredID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CounteredBy SET CounteredByTotalDownVote = CounteredByTotalDownVote - 1 WHERE CounteredID = %s",(counterid,))
        cur.execute("INSERT INTO CounteredByVote(UserID, CounteredID, CounteredUpVote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CounteredBy SET CounteredByTotalUpVote = CounteredByTotalUpVote + 1 WHERE CounteredID = %s",(counterid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM CounteredByVote WHERE CounteredID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CounteredBy SET CounteredTotalUpVote = CounteredTotalUpVote - 1 WHERE CounteredID = %s",(counterid,))
        mysql.connection.commit()

# FUNCTION TO DOWN VOTE ON THE COUNTERED BY SECTION
def counteredbydownvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    counterid = uservote['counterid']

    cur.execute('SELECT CounteredUpVote, CounteredDownVote FROM CounteredByVote WHERE CounteredID = %s AND UserID = %s',(counterid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO CounteredByVote(UserID, CounteredID, CounteredDownVote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CounteredBy SET CounteredTotalDownVote = CounteredTotalDownVote + 1 WHERE CounteredID = %s",(counterid,))
        mysql.connection.commit()
        return redirect(request.url)

    if a[0] == 1:
        cur.execute("DELETE FROM CounteredByVote WHERE CounteredID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CounteredBy SET CounteredTotalUpVote = CounteredTotalUpVote - 1 WHERE CounteredID = %s",(counterid,))
        cur.execute("INSERT INTO CounteredByVote(UserID, CounteredID, CounteredDownVote) VALUES(%s,%s,%s)",(user, counterid, vote))
        cur.execute("UPDATE CounteredBy SET CounteredTotalDownVote = CounteredTotalDownVote + 1 WHERE CounteredID = %s",(counterid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM CounteredByVote WHERE CounteredID = %s AND UserID = %s",(counterid, user))
        cur.execute("UPDATE CounteredBy SET CounteredTotalDownVote = CounteredTotalDownVote - 1 WHERE CounteredID = %s",(counterid,))
        mysql.connection.commit()

# FUNCTION TO RETURN TOTAL VOTES OF EACH COUNTERED BY ENTRY
def counteredbytotalvotes(cur):
    cur.execute("SELECT CounteredByTotalVotes, CounteredID FROM CounteredBy")
    votes = cur.fetchall()
    return votes

# FUNCTION TO ADD ITEM TO BUY FOR HERO TO HERO PAGE
def additemfor(cur):
    user = session['id']
    itemforinfo = request.form
    name = itemforinfo['itemforname']
    info = itemforinfo['itemforinfo']
    tag = itemforinfo['itemfortag']
    hid = itemforinfo['itemforheroid']
    cur.execute("INSERT INTO HeroItemsFor(ItemID, HeroItemForUserInfo, UserID, ItemForTag, HeroID) VALUES(%s, %s, %s, %s, %s)",(name, info, user, tag, hid))
    mysql.connection.commit()

# FUNCTION TO ADD ITEM TO BUY AGAINST HERO TO HERO PAGE
def additemagainst(cur):
    user = session['id']
    itemagainstinfo = request.form
    name = itemagainstinfo['itemagainstname']
    info = itemagainstinfo['itemagainstinfo']
    tag = itemagainstinfo['itemagainsttag']
    hid = itemagainstinfo['itemagainstheroid']
    cur.execute("INSERT INTO HeroItemsAgainst(ItemID, HeroItemAgainstUserInfo, UserID, ItemAgainstTag, HeroID) VALUES(%s, %s, %s, %s, %s)",(name, info, user, tag, hid))
    mysql.connection.commit()

# FUNCTION TO UP VOTE ON THE ITEM FOR SECTION
def itemforupvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    itemforid = uservote['itemforid']

    cur.execute('SELECT HeroItemForUpVote, HeroItemForDownVote FROM HeroItemsForVote WHERE HeroItemForID = %s AND UserID = %s',(itemforid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO HeroItemsForVote(UserID, HeroItemForID, HeroItemForUpVote) VALUES(%s,%s,%s)",(user, itemforid, vote))
        cur.execute("UPDATE HeroItemsFor SET HeroItemForTotalUpVote = HeroItemForTotalUpVote + 1 WHERE HeroItemForID = %s",(itemforid,))
        mysql.connection.commit()
        return redirect(request.url)
    
    if a[1] == 1:
        cur.execute("DELETE FROM HeroItemsForVote WHERE HeroItemForID = %s AND UserID = %s",(itemforid, user))
        cur.execute("UPDATE HeroItemsFor SET HeroItemForTotalDownVote = HeroItemForTotalDownVote - 1 WHERE HeroItemForID = %s",(itemforid,))
        cur.execute("INSERT INTO HeroItemsForVote(UserID, HeroItemForID, HeroItemForUpVote) VALUES(%s,%s,%s)",(user, itemforid, vote))
        cur.execute("UPDATE HeroItemsFor SET HeroItemForTotalUpVote = HeroItemForTotalUpVote + 1 WHERE HeroItemForID = %s",(itemforid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM HeroItemsForVote WHERE HeroItemForID = %s AND UserID = %s",(itemforid, user))
        cur.execute("UPDATE HeroItemsFor SET HeroItemForTotalUpVote = HeroItemForTotalUpVote - 1 WHERE HeroItemForID = %s",(itemforid,))
        mysql.connection.commit()
        
# FUNCTION TO DOWN VOTE ON THE ITEM FOR SECTION
def itemfordownvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    itemforid = uservote['itemforid']

    cur.execute('SELECT HeroItemForUpVote, HeroItemForDownVote FROM HeroItemsForVote WHERE HeroItemForID = %s AND UserID = %s',(itemforid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO HeroItemsForVote(UserID, HeroItemForID, HeroItemForDownVote) VALUES(%s,%s,%s)",(user, itemforid, vote))
        cur.execute("UPDATE HeroItemsFor SET HeroItemForTotalDownVote = HeroItemForTotalDownVote + 1 WHERE HeroItemForID = %s",(itemforid,))
        mysql.connection.commit()
        return redirect(request.url)

    if a[0] == 1:
        cur.execute("DELETE FROM HeroItemsForVote WHERE HeroItemForID = %s AND UserID = %s",(itemforid, user))
        cur.execute("UPDATE HeroItemsFor SET HeroItemForTotalUpVote = HeroItemForTotalUpVote - 1 WHERE HeroItemForID = %s",(itemforid,))
        cur.execute("INSERT INTO HeroItemsForVote(UserID, HeroItemForID, HeroItemForDownVote) VALUES(%s,%s,%s)",(user, itemforid, vote))
        cur.execute("UPDATE HeroItemsFor SET HeroItemForTotalDownVote = HeroItemForTotalDownVote + 1 WHERE HeroItemForID = %s",(itemforid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM HeroItemsForVote WHERE HeroItemForID = %s AND UserID = %s",(itemforid, user))
        cur.execute("UPDATE HeroItemsFor SET HeroItemForTotalDownVote = HeroItemForTotalDownVote - 1 WHERE HeroItemForID = %s",(itemforid,))
        mysql.connection.commit()
    
# # FUNCTION TO UP VOTE ON THE ITEM AGAINST SECTION
def itemagainstupvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    itemagainstid = uservote['itemagainstid']

    cur.execute('SELECT HeroItemAgainstUpVote, HeroItemAgainstDownVote FROM HeroItemsAgainstVote WHERE HeroItemAgainstID = %s AND UserID = %s',(itemagainstid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO HeroItemsAgainstVote(UserID, HeroItemAgainstID, HeroItemAgainstUpVote) VALUES(%s,%s,%s)",(user, itemagainstid, vote))
        cur.execute("UPDATE HeroItemsAgainst SET HeroItemAgainstTotalUpVote = HeroItemAgainstTotalUpVote + 1 WHERE HeroItemAgainstID = %s",(itemagainstid,))
        mysql.connection.commit()
        return redirect(request.url)
    
    if a[1] == 1:
        cur.execute("DELETE FROM HeroItemsAgainstVote WHERE HeroItemAgainstID = %s AND UserID = %s",(itemagainstid, user))
        cur.execute("UPDATE HeroItemsAgainst SET HeroItemAgainstTotalDownVote = HeroItemAgainstTotalDownVote - 1 WHERE HeroItemAgainstID = %s",(itemagainstid,))
        cur.execute("INSERT INTO HeroItemsAgainstVote(UserID, HeroItemAgainstID, HeroItemAgainstUpVote) VALUES(%s,%s,%s)",(user, itemagainstid, vote))
        cur.execute("UPDATE HeroItemsAgainst SET HeroItemAgainstTotalUpVote = HeroItemAgainstTotalUpVote + 1 WHERE HeroItemAgainstID = %s",(itemagainstid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM HeroItemsAgainstVote WHERE HeroItemAgainstID = %s AND UserID = %s",(itemagainstid, user))
        cur.execute("UPDATE HeroItemsAgainst SET HeroItemAgainstTotalUpVote = HeroItemAgainstTotalUpVote - 1 WHERE HeroItemAgainstID = %s",(itemagainstid,))
        mysql.connection.commit()

# # FUNCTION TO DOWN VOTE ON THE ITEM AGAINST SECTION
def itemagainstdownvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    itemagainstid = uservote['itemagainstid']

    cur.execute('SELECT HeroItemAgainstUpVote, HeroItemAgainstDownVote FROM HeroItemsAgainstVote WHERE HeroItemAgainstID = %s AND UserID = %s',(itemagainstid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO HeroItemsAgainstVote(UserID, HeroItemAgainstID, HeroItemAgainstDownVote) VALUES(%s,%s,%s)",(user, itemagainstid, vote))
        cur.execute("UPDATE HeroItemsAgainst SET HeroItemAgainstTotalDownVote = HeroItemAgainstTotalDownVote + 1 WHERE HeroItemAgainstID = %s",(itemagainstid,))
        mysql.connection.commit()
        return redirect(request.url)

    if a[0] == 1:
        cur.execute("DELETE FROM HeroItemsAgainstVote WHERE HeroItemAgainstID = %s AND UserID = %s",(itemagainstid, user))
        cur.execute("UPDATE HeroItemsAgainst SET HeroItemAgainstTotalUpVote = HeroItemAgainstTotalUpVote - 1 WHERE HeroItemAgainstID = %s",(itemagainstid,))
        cur.execute("INSERT INTO HeroItemsAgainstVote(UserID, HeroItemAgainstID, HeroItemAgainstDownVote) VALUES(%s,%s,%s)",(user, itemagainstid, vote))
        cur.execute("UPDATE HeroItemsAgainst SET HeroItemAgainstTotalDownVote = HeroItemAgainstTotalDownVote + 1 WHERE HeroItemAgainstID = %s",(itemagainstid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM HeroItemsAgainstVote WHERE HeroItemAgainstID = %s AND UserID = %s",(itemagainstid, user))
        cur.execute("UPDATE HeroItemsAgainst SET HeroItemAgainstTotalDownVote = HeroItemAgainstTotalDownVote - 1 WHERE HeroItemAgainstID = %s",(itemagainstid,))
        mysql.connection.commit()
    
# FUNCTION TO RETURN TOTAL VOTES ON ITEMS TO BUY FOR SECTION
def itemfortotalvotes(cur):
    cur.execute("SELECT HeroItemForTotalVotes, HeroItemForID FROM HeroItemsFor")
    votes = cur.fetchall()
    return votes

# FUNCTION TO RETURN TOTAL VOTES ON ITEMS TO BUY AGAINST SECTION
def itemagainsttotalvotes(cur):
    cur.execute("SELECT HeroItemAgainstTotalVotes, HeroItemAgainstID FROM HeroItemsAgainst")
    votes = cur.fetchall()
    return votes

# FUNCTION TO UP VOTE NOTES ON ABILITIES
def abilityupvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    abilityinfoid = uservote['abilityinfoid']

    cur.execute('SELECT AbilityUpVote, AbilityDownVote FROM AbilityVote WHERE AbilityInfoID = %s AND UserID = %s',(abilityinfoid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO AbilityVote(UserID, AbilityInfoID, AbilityUpVote) VALUES(%s,%s,%s)",(user, abilityinfoid, vote))
        cur.execute("UPDATE AbilityInfo SET AbilityTotalUpVote = AbilityTotalUpVote + 1 WHERE AbilityInfoID = %s",(abilityinfoid,))
        mysql.connection.commit()
        return redirect(request.url)
    
    if a[1] == 1:
        cur.execute("DELETE FROM AbilityVote WHERE AbilityInfoID = %s AND UserID = %s",(abilityinfoid, user))
        cur.execute("UPDATE AbilityInfo SET AbilityTotalDownVote = AbilityTotalDownVote - 1 WHERE AbilityInfoID = %s",(abilityinfoid,))
        cur.execute("INSERT INTO AbilityVote(UserID, AbilityInfoID, AbilityUpVote) VALUES(%s,%s,%s)",(user, abilityinfoid, vote))
        cur.execute("UPDATE AbilityInfo SET AbilityTotalUpVote = AbilityTotalUpVote + 1 WHERE AbilityInfoID = %s",(abilityinfoid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM AbilityVote WHERE AbilityInfoID = %s AND UserID = %s",(abilityinfoid, user))
        cur.execute("UPDATE AbilityInfo SET AbilityTotalUpVote = AbilityTotalUpVote - 1 WHERE AbilityInfoID = %s",(abilityinfoid,))
        mysql.connection.commit()

# FUNCTION TO DOWN VOTE NOTES ON ABILITIES
def abilitydownvote(cur):
    user = session['id']
    uservote = request.form
    vote = uservote['bool']
    abilityinfoid = uservote['abilityinfoid']

    cur.execute('SELECT AbilityUpVote, AbilityDownVote FROM AbilityVote WHERE AbilityInfoID = %s AND UserID = %s',(abilityinfoid, user))
    a = cur.fetchone()

    if a is None:
        cur.execute("INSERT INTO AbilityVote(UserID, AbilityInfoID, AbilityDownVote) VALUES(%s,%s,%s)",(user, abilityinfoid, vote))
        cur.execute("UPDATE AbilityInfo SET AbilityTotalDownVote = AbilityTotalDownVote + 1 WHERE AbilityInfoID = %s",(abilityinfoid,))
        mysql.connection.commit()
        return redirect(request.url)

    if a[0] == 1:
        cur.execute("DELETE FROM AbilityVote WHERE AbilityInfoID = %s AND UserID = %s",(abilityinfoid, user))
        cur.execute("UPDATE AbilityInfo SET AbilityTotalUpVote = AbilityTotalUpVote - 1 WHERE AbilityInfoID = %s",(abilityinfoid,))
        cur.execute("INSERT INTO AbilityVote(UserID, AbilityInfoID, AbilityDownVote) VALUES(%s,%s,%s)",(user, abilityinfoid, vote))
        cur.execute("UPDATE AbilityInfo SET AbilityTotalDownVote = AbilityTotalDownVote + 1 WHERE AbilityInfoID = %s",(abilityinfoid,))
        mysql.connection.commit()

    else:
        cur.execute("DELETE FROM AbilityVote WHERE AbilityInfoID = %s AND UserID = %s",(abilityinfoid, user))
        cur.execute("UPDATE AbilityInfo SET AbilityTotalDownVote = AbilityTotalDownVote - 1 WHERE AbilityInfoID = %s",(abilityinfoid,))
        mysql.connection.commit()

# FUNCTION TO RETURN TOTAL VOTES OF EACH COUNTERED BY ENTRY
def abilitytotalvotes(cur):
    cur.execute("SELECT AbilityTotalVotes, AbilityInfoID FROM AbilityInfo")
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

@app.route('/items')
def items():
    return render_template("itempool.html")

@app.route('/items/<itemname>', methods=['GET', 'POST'])
def item(itemname):
  
    cur = mysql.connection.cursor()
    cur.execute("SELECT ItemID, ItemName, ItemIconLink, ItemCost, ItemInfo, ItemAbilityName1, ItemAbilityInfo1, ItemAbilityName2, ItemAbilityInfo2, ItemAbilityName3, ItemAbilityInfo3 FROM Items")
    items = cur.fetchall()

    itemid = None
    iname = None
    itemimgurl = None
    itemcost = None
    iteminfo = None
    abilityname1 = None
    abilityinfo1 = None
    abilityname2 = None
    abilityinfo2 = None
    abilityname3 = None
    abilityinfo3 = None
    
    for i in items:
        if i[1] == itemname:
            itemid = i[0]
            iname = i[1]
            itemimgurl = i[2]
            itemcost = i[3]
            iteminfo = i[4]
            abilityname1 = i[5]
            abilityinfo1 = i[6]
            abilityname2 = i[7]
            abilityinfo2 = i[8]
            abilityname3 = i[9]
            abilityinfo3 = i[10]

    iteminfo = iteminfo.split(',')

    iname = string.capwords(iname.replace('-',' '))

    cur.execute("SELECT Heroes.HeroIconLink, HeroItemsFor.ItemID, HeroItemsFor.ItemForTag, HeroItemsFor.HeroItemForUserInfo, HeroItemsFor.HeroItemForTotalVotes FROM Heroes INNER JOIN HeroItemsFor ON HeroItemsFor.HeroID=Heroes.HeroID ORDER BY HeroItemForTotalVotes DESC")
    itemsfor = cur.fetchall()

    cur.execute("SELECT Heroes.HeroIconLink, HeroItemsAgainst.ItemID, HeroItemsAgainst.ItemAgainstTag, HeroItemsAgainst.HeroItemAgainstUserInfo, HeroItemsAgainst.HeroItemAgainstTotalVotes FROM Heroes INNER JOIN HeroItemsAgainst ON HeroItemsAgainst.HeroID=Heroes.HeroID ORDER BY HeroItemAgainstTotalVotes DESC")
    itemsagainst = cur.fetchall()

    cur.close()

    return render_template("item.html",items=items, itemid=itemid, iname=iname, imgurl=itemimgurl, itemsfor=itemsfor, itemsagainst=itemsagainst, itemcost=itemcost, iteminfo=iteminfo, abilityname1=abilityname1, abilityname2=abilityname2, abilityname3=abilityname3, abilityinfo1=abilityinfo1, abilityinfo2=abilityinfo2, abilityinfo3=abilityinfo3)

@app.route('/heroes/<heroname>', methods=['GET', 'POST'])
def hero(heroname):

    cur = mysql.connection.cursor()
    cur.execute("SELECT HeroID, HeroName, HeroIconLink, HeroAttribute, HeroStrength, HeroAgility, HeroIntelligence, HeroArmor, HeroAttack, MovementSpeed, HeroHealth, HeroMana, HeroAttackType, Complexity, HeroRole1, HeroRole2, HeroRole3, HeroRole4, HeroRole5, HeroRole6, HeroLane1, HeroLane2, HeroLane3, HeroLane4 FROM Heroes")
    heroes = cur.fetchall()
    
    hname = None
    heroimgurl = None
    hid = None
    heroattribute = None
    strength = None
    agility = None
    intelligence = None
    armor = None
    attack = None
    speed = None
    health = None
    mana = None
    type = None
    complexity = None
    role1 = None
    role2 = None
    role3 = None
    role4 = None
    role5 = None
    role6 = None
    lane1 = None
    lane2 = None
    lane3 = None
    lane4 = None


    for i in heroes:
        if i[1] == heroname:
            hid = i[0]
            hname = i[1]
            heroimgurl = i[2]
            heroattribute = i[3]
            strength = i[4]
            agility = i[5]
            intelligence = i[6] 
            armor = i[7]
            attack = i[8]
            speed = i[9]
            health = i[10]
            mana = i[11]
            type = i[12]
            complexity = i[13]
            role1 = i[14]
            role2 = i[15]
            role3 = i[16]
            role4 = i[17]
            role5 = i[18]
            role6 = i[19]         
            lane1 = i[20]
            lane2 = i[21]
            lane3 = i[22]
            lane4 = i[23]   
        
    hname = string.capwords(hname.replace('-',' '))

    # FETCH ABILITIES
    cur.execute("SELECT Heroes.HeroName, Abilities.HeroID, Abilities.AbilityName, Abilities.AbilityIconLink, Abilities.AbilityDesc, Abilities.AbilityAbility, Abilities.AbilityAffect, Abilities.AbilityDamage, Abilities.AbilityCooldown, Abilities.AbilityManaCost, Abilities.AbilityID FROM Heroes INNER JOIN Abilities ON Abilities.HeroID=Heroes.HeroID")
    abilities = cur.fetchall()

    # FETCH ABILITY USER INFO
    cur.execute("SELECT AbilityID, UserID, AbilityUserInfo, AbilityTag, AbilityInfoID FROM AbilityInfo ORDER BY AbilityTotalVotes DESC")
    fetchabilityuserinfo = cur.fetchall()

    # FETCH HERO INFO
    cur.execute("SELECT HeroID,HeroName FROM Heroes")
    fetchnames = cur.fetchall()

    # FETCH COUNTERS
    cur.execute("SELECT Heroes.HeroIconLink, CountersTo.CounterUserInfo, Heroes.HeroName, CountersTo.CounterID, CountersTo.CounterTag FROM Heroes INNER JOIN CountersTo ON CountersTo.HeroID=Heroes.HeroID ORDER BY CounterToTotalVotes DESC")
    fetchcounterto = cur.fetchall()

    # FETCH COUNTERED BY
    cur.execute("SELECT Heroes.HeroIconLink, CounteredBy.CounteredUserInfo, Heroes.HeroName, CounteredBy.CounteredID, CounteredBy.CounteredTag FROM Heroes INNER JOIN CounteredBy ON CounteredBy.HeroID=Heroes.HeroID ORDER BY CounteredByTotalVotes DESC")
    fetchcounteredby = cur.fetchall()

    # FETCH ITEMS INFO
    cur.execute("SELECT ItemID,ItemName FROM Items")
    fetchitems = cur.fetchall()

    # FETCH ITEMS FOR
    cur.execute("SELECT Items.ItemIconLink, HeroItemsFor.HeroItemForUserInfo, Items.ItemName, HeroItemsFor.HeroItemForID, HeroItemsFor.ItemForTag FROM Items INNER JOIN HeroItemsFor ON HeroItemsFor.ItemID=Items.ItemID ORDER BY HeroItemForTotalVotes DESC")
    fetchitemsfor = cur.fetchall()

    # FETCH ITEMS AGAINST
    cur.execute("SELECT Items.ItemIconLink, HeroItemsAgainst.HeroItemAgainstUserInfo, Items.ItemName, HeroItemsAgainst.HeroItemAgainstID, HeroItemsAgainst.ItemAgainstTag FROM Items INNER JOIN HeroItemsAgainst ON HeroItemsAgainst.ItemID=Items.ItemID ORDER BY HeroItemAgainstTotalVotes DESC")
    fetchitemsagainst = cur.fetchall()

    fetchtotalcountervotes = countertototalvotes(cur)
    fetchtotalcounteredvotes = counteredbytotalvotes(cur)
    fetchtotalitemforvotes = itemfortotalvotes(cur)
    fetchtotalitemagainstvotes = itemagainsttotalvotes(cur)
    abilityvotes = abilitytotalvotes(cur)

    if "countertosubmit" in request.form:
        addcounterto(cur)
        return redirect(request.url)
    if "counteredbysubmit" in request.form:
        addcounteredby(cur)
        return redirect(request.url)
    if "counterupvote" in request.form:
        countertoupvote(cur)
        return redirect(request.url)
    if "counterdownvote" in request.form:
        countertodownvote(cur)
        return redirect(request.url)
    if "counteredupvote" in request.form:
        counteredbyupvote(cur)
        return redirect(request.url)
    if "countereddownvote" in request.form:
        counteredbydownvote(cur)
        return redirect(request.url)
    if "itemforsubmit" in request.form:
        additemfor(cur)
        return redirect(request.url)
    if "itemagainstsubmit" in request.form:
        additemagainst(cur)
        return redirect(request.url)
    if "itemforupvote" in request.form:
        itemforupvote(cur)
        return redirect(request.url)
    if "itemfordownvote" in request.form:
        itemfordownvote(cur)
        return redirect(request.url)
    if "itemagainstupvote" in request.form:
        itemagainstupvote(cur)
        return redirect(request.url)
    if "itemagainstdownvote" in request.form:
        itemagainstdownvote(cur)
        return redirect(request.url)
    if "abilityinfosubmit" in request.form:
        addabilityinfo(cur)
        return redirect(request.url)
    if "abilityupvote" in request.form:
        abilityupvote(cur)
        return redirect(request.url)
    if "abilitydownvote" in request.form:
        abilitydownvote(cur)
        return redirect(request.url)


    cur.close()
   
    return render_template("hero.html", hname=hname, heroimgurl=heroimgurl, heroes=heroes, heronames=fetchnames, countertoinfo=fetchcounterto, counteredbyinfo=fetchcounteredby, countertotalvotes=fetchtotalcountervotes, 
    counteredtotalvotes=fetchtotalcounteredvotes, items=fetchitems, itemsfor=fetchitemsfor, itemsagainst=fetchitemsagainst, itemforvotes=fetchtotalitemforvotes, itemagainstvotes=fetchtotalitemagainstvotes, abilities=abilities, hid=hid,
    heroattribute=heroattribute, strength=strength, agility=agility, intelligence=intelligence, role1=role1, role2=role2, role3=role3, role4=role4, role5=role5,role6=role6, armor=armor, attack=attack, speed=speed,
    type=type, complexity=complexity,lane1=lane1, lane2=lane2, lane3=lane3, lane4=lane4, health=health, mana=mana, abilityuserinfo=fetchabilityuserinfo,abilityvotes=abilityvotes)

if __name__ == '__main__':
    app.run(debug=True)
