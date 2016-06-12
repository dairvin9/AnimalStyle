from app import app, db

# Enable search if python 2 is running
import sys

if sys.version_info >= (3, 0):
    enable_search = False
else:
    enable_search = True
    import flask_whooshalchemy as whooshalchemy


class BlogPost(db.Model):
    # What is searchable for the article
    __searchable__ = ['content','title']

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    title_no_spaces = db.Column(db.String(64), index=True, unique=True)  # used for url
    comments = db.relationship('Comment', backref='comment', lazy='dynamic')  # comments
    content = db.Column(db.String(1000), index=True)
    timestamp = db.Column(db.DateTime)
    date_string = db.Column(db.String(64), index=True, unique=True)

    def __repr__(self):
        return '<BlogPost %r>' % (self.title)

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(64), index=True)
    text = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    blogpost_id = db.Column(db.Integer, db.ForeignKey('blog_post.id'))

    def __repr__(self):
        return '<Comment: %r says %r>' % (self.author, self.text)

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3


class CodeProject(db.Model):
    # Representation of the coding project

    __searchable__ = ['name', 'description']

    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(64), index=True, unique=True)
    description = db.Column(db.String(1000), index=True)
    timestamp = db.Column(db.DateTime)
    github_link = db.Column(db.String(150), index=True)
    download_link = db.Column(db.String(64), index=True)
    pictures = db.relationship('Picture', backref='picture', lazy='dynamic')  # pictures
    title_no_spaces = db.Column(db.String(64), index=True, unique=True)  # used for url
    date_string = db.Column(db.String(64), index=True)

    def __repr__(self):
        return '<CodeProject %r>' % (self.name)

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3


class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    link = db.Column(db.String(150), index=True, unique=True)
    foreign_id = db.Column(db.Integer, db.ForeignKey('code_project.id'))

    def __repr__(self):
        return '<Picture %r>' % (self.link)

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

# Enable search if running python 2
if enable_search:
    whooshalchemy.whoosh_index(app, BlogPost)
    whooshalchemy.whoosh_index(app, CodeProject)