from flask import render_template, url_for, flash, redirect
from project import app
from project.forms import RegistrationForm, LoginForm
from project.models import User, Post 

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
