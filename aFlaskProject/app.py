from flask import Flask, render_template, flash, redirect, url_for, session, logging, request
from quotes import Quotes #The Data
from flaskext.mysql import MySQL
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from passlib.hash import sha256_crypt
from functools import wraps

app = Flask(__name__)

mysql = MySQL()

#Config MySQL
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345'
app.config['MYSQL_DATABASE_DB'] = 'flaskdb'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

#Initialize MySQL
mysql.init_app(app)
con = mysql.connect()
cursor = con.cursor()

the_quotes = Quotes()
print the_quotes

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/quotes')
def quotes():
    return render_template('quotes.html', quotes=the_quotes)

@app.route('/quote/<string:id>&<string:painter>&<string:body>')
def quote(id,painter,body):
    return render_template('quote.html',id=id,painter=painter,body=body)

class RegisterForm(Form):
    name = StringField('Name', validators=[validators.Length(min=1,max=50)])
    username = StringField('Username', validators=[validators.Length(min=4,max=25)])
    email = StringField('Email',validators=[validators.Length(min=6,max=30)])
    password = PasswordField('Password', validators=[validators.DataRequired(),
                                                  validators.EqualTo('confirm','Passwords do not match')])
    confirm = PasswordField('Confirm Password')

@app.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        name = form.name.data
        username = form.username.data
        email = form.email.data
        password = sha256_crypt.encrypt(str(form.password.data))

        query = "INSERT INTO users (name, username, email, password) VALUES ('%s', '%s','%s', '%s')" % (name, username, email, password)
        #print query

        cursor.execute(query)
        con.commit()
        #cursor.close()

        flash("You are now registered", "success")

        return redirect(url_for("index"))
        #return render_template('register.html')
    return render_template('register.html', form=form)

def user_logged_in(u):
    @wraps(u)
    def wrapped(*args, **kwargs):
        if 'logged_in' in session:
            return u(*args, **kwargs)
        else:
            flash('Unauthorized!','danger')
            return redirect(url_for('login'))
    return wrapped

@app.route('/dashboard')
@user_logged_in
def dashboard():
    return render_template('dashboard.html',quotes=the_quotes)

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password_check = request.form['password']
        print username, password_check

        cur = con.cursor()
        query = "SELECT * FROM users WHERE username = '%s'" % username
        print query
        result = cur.execute(query)
        print "result=", result
        if result>0:
            data = cur.fetchone()
            password = data[4]
            print "Password=", password
            if sha256_crypt.verify(password_check,password):
                print 'PASSWORD MATCHED'
                app.logger.info('PASSWORD MATCHED')
                session['logged_in'] = True
                session['username'] = username
                flash('You are Logged In','success')
                return redirect(url_for('dashboard'))
            else:
                print 'PASSWORD NOT MATCHED'
                app.logger.info('PASSWORD DONT MATCHED')
                error = "Invalid Password"
                return render_template('login.html', error = error)
            cur.close()
        else:
            print 'NO SUCH USER'
            app.logger.info('NO SUCH USER')
            error = "Invalid Username"
            return render_template('login.html',error = error)
    else:
        print "NO POST"
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You are Logged Out','success')
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.secret_key='theSecretKey'
    app.run(debug=True)


