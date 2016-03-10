from flask import Flask, render_template, redirect, url_for, request, session, flash, g
from functools import wraps
import sqlite3

app = Flask(__name__)
app.database = "sample.db"

app.secret_key = 'my secret_key'

# login required decorator
def login_required(f):
    @wraps(f)
    def wrap(*args, **kwargs):
        if 'logging_in' in session:
            return f(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap

@app.route('/')
@login_required
def home():
	g.db = connect_db()
	cur = g.db.execute('select * from posts')
	# print cur
	# print cur.fetchall
	# post_dict = {}
	posts = []

	for row in cur.fetchall():
		posts.append(dict(title=row[0], description=row[1]))
		print posts

	g.db.close() 
	return render_template('index.html', posts=posts)

@app.route('/welcome')
def welcome():
    return render_template('welcome.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
	error = None
	if request.method == 'POST':
		if request.form.get('username') != "admin" and request.form.get('passowrd') != "admin":
		    error = 'Invaild credentials, please try again'
		else:
			session['logging_in'] = True
			flash('You were just logged in')
			return redirect(url_for('home'))
	return render_template('login.html', error=error)

@app.route('/logout')
@login_required
def logout():
	session.pop('logging_in', None)
	flash('You werer just logged out')
	return redirect(url_for('welcome'))

def connect_db():
	return sqlite3.connect(app.database)

if __name__=='__main__':
    app.run(debug=True)