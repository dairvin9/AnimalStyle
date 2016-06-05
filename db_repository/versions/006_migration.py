from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
blog_post = Table('blog_post', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('title', VARCHAR(length=64)),
    Column('content', VARCHAR(length=1000)),
    Column('timestamp', DATETIME),
)

comment = Table('comment', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('author', VARCHAR(length=64)),
    Column('text', VARCHAR(length=280)),
    Column('post_id', INTEGER),
    Column('timestamp', DATETIME),
)

post = Table('post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('body', String(length=140)),
    Column('timestamp', DateTime),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['blog_post'].drop()
    pre_meta.tables['comment'].drop()
    post_meta.tables['post'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['blog_post'].create()
    pre_meta.tables['comment'].create()
    post_meta.tables['post'].drop()
    post_meta.tables['user'].drop()
