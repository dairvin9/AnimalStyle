from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
code_project = Table('code_project', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('name', VARCHAR(length=64)),
    Column('description', VARCHAR(length=1000)),
    Column('timestamp', DATETIME),
    Column('github_link', VARCHAR(length=150)),
    Column('download_link', VARCHAR(length=64)),
    Column('title_no_spaces', VARCHAR(length=64)),
    Column('date_string', VARCHAR(length=64)),
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
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['code_project'].columns['title_no_spaces'].drop()
    post_meta.tables['code_project'].columns['name_no_spaces'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['code_project'].columns['title_no_spaces'].create()
    post_meta.tables['code_project'].columns['name_no_spaces'].drop()
