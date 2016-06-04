from flask import render_template, flash, redirect
from app import app
from .forms import CommentForm

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/base')
def base():
    return render_template('base.html')

@app.route('/blog', methods=['GET', 'POST'])
def blog():
    form = CommentForm()
    return render_template('blog.html',
                           form=form)

@app.route('/')
@app.route('/code_projects')
def code_projects():
    return render_template('code_projects.html')

# for debugging. Never to be used publicly, lol
@app.route('/comment', methods=['GET', 'POST'])
def comment():
    form = CommentForm()
    return render_template('comment.html',
                           form=form)

@app.route('/blog_post', methods=['GET', 'POST'])
def blog_post():
    form = CommentForm()
    if form.validate_on_submit():
        flash('Comment Recieved') # Currently does not show
        return redirect('/blog_post')
    return render_template('blog_post.html',
                           form=form)