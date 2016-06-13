from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
blog_post = Table('blog_post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('title_no_spaces', String(length=64)),
    Column('content', String(length=1000)),
    Column('timestamp', DateTime),
    Column('date_string', String(length=64)),
    Column('picture', String(length=150)),
    Column('short_description', String(length=140)),
)

code_project = Table('code_project', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('description', String(length=1000)),
    Column('timestamp', DateTime),
    Column('github_link', String(length=150)),
    Column('download_link', String(length=64)),
    Column('name_no_spaces', String(length=64)),
    Column('date_string', String(length=64)),
    Column('short_description', String(length=140)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['blog_post'].columns['short_description'].create()
    post_meta.tables['code_project'].columns['short_description'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['blog_post'].columns['short_description'].drop()
    post_meta.tables['code_project'].columns['short_description'].drop()
