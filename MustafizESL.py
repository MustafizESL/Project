from datetime import datetime
from flask import Flask, render_template, url_for, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm



app = Flask(__name__)

app.config['SECRET_KEY'] = 'e5b1a8127f65c1bd220a69b3379ef33d'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	image_file = db.Column(db.String(20), nullable=False, default='default.jpg')
	password = db.Column(db.String(60), nullable=False)
	posts = db.relationship('Post', backref='author', lazy=True)

	def __repr__(self):
		return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100), nullable=False)
	date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	content = db.Column(db.Text, nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

	def __repr__(self):
		return f"Post('{self.title}', '{self.date_posted}')"

 

posts = [
	{
		'author': 'Mustafiz',
		'title': 'How I Mastered American Accent!',
		'content': 'It was 2015. I used to struggle to understand native speakers, but I really wanted to speak like a native American. So, I started listening everyday. I listened to natural conversations of highly educated American language experts. I tried to copy them and I just loved it. After 2 months, I realized that my pronunciation was almost like a native American. I was surprised when I listened to my own voice which was recorded three months ago. I couldn\'t believe it!',
		'date_posted': 'January 19, 2021'
	},
	{
		'author': 'Test User',
		'title': 'Post 2',
		'content': 'Second post content',
		'date_posted': 'January 19, 2021'
	}
]
 
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title = 'About')


@app.route("/register", methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		flash(f'Account created for {form.username.data}!', 'success')
		return redirect(url_for('home'))
	return render_template('register.html', title='Register', form=form)



@app.route("/login")
def login():
	form = LoginForm()
	return render_template('login.html', title='Login', form=form)


if __name__ == "__main__":
	app.run(debug=True)
