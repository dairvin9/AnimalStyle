from flask import render_template, flash, redirect
from app import app
from .forms import CommentForm
from .models import BlogPost, Comment


# Helper Functions to get things out of the database
# Dont know if I need this


# Sets up the url and functions that load html pages

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

@app.route('/blog')
def blog():
    return render_template('blog.html')

# Figure out how to allow multiple different of these pages to trigger different things
@app.route('/blog_post/<blog_title>', methods=['GET', 'POST'])
def blog_post(blog_title):
    b = BlogPost(title="Bash Script Basics", content="In Progress") # Fake BlogPost, deal with it
    b = BlogPost.query.filter_by(title=blog_title).first() #should grab first blog post to match title
    c = [Comment(author='Steve',text="What a blog!"),Comment(author='Jason',text="Bash scripting is not useful")] #fake comments list
    #c = Comment.query.filter_by(blogpost_id=b.id) # should grab all the comments on this post
    form = CommentForm()
    if form.validate_on_submit():
        flash('Comment Recieved') # Currently does not show
        return redirect('/blog_post')
    return render_template('blog_post.html',
                           blog_post=b,
                           comments=c,
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

