from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
code_project = Table('code_project', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('name', String(length=64)),
    Column('description', String(length=1000)),
    Column('timestamp', DateTime),
    Column('github_link', String(length=150)),
    Column('download_link', String(length=64)),
    Column('title_no_spaces', String(length=64)),
    Column('date_string', String(length=64)),
)

picture = Table('picture', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('link', String(length=150)),
    Column('foreign_id', Integer),
)

blog_post = Table('blog_post', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('title', String(length=64)),
    Column('title_no_spaces', String(length=64)),
    Column('content', String(length=1000)),
    Column('timestamp', DateTime),
    Column('date_string', String(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['code_project'].create()
    post_meta.tables['picture'].create()
    post_meta.tables['blog_post'].columns['date_string'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['code_project'].drop()
    post_meta.tables['picture'].drop()
    post_meta.tables['blog_post'].columns['date_string'].drop()
