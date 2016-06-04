from app import db

class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64), index=True, unique=True)
    content = db.Column(db.String(1000), index=True, unique=True)
    comments = db.relationship('Comment',backref='comment',lazy='dynamic')
    timestamp = db.Column(db.DateTime)

    def __repr__(self):
        return '<BlogPost %r>' % (self.title)


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String(64), index=True)
    text = db.Column(db.String(280))
    timestamp = db.Column(db.DateTime)
    post_id = db.Column(db.Integer, db.ForeignKey('BlogPost.id'))

    def __repr__(self):
        return '<Comment %r>' % (self.id)