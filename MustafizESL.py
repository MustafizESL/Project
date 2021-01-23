from flask import Flask, render_template, url_for
app = Flask(__name__)

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


if __name__ == "__main__":
	app.run(debug=True)
