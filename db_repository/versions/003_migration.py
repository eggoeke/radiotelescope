from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
reserved = Table('reserved', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('telescope', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

reserved = Table('reserved', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('telescope', String(length=140)),
    Column('time', DateTime),
    Column('user_id', Integer),
)

waitlist = Table('waitlist', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('telescope', VARCHAR(length=140)),
    Column('timestamp', DATETIME),
    Column('user_id', INTEGER),
)

waitlist = Table('waitlist', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('telescope', String(length=140)),
    Column('time', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reserved'].columns['timestamp'].drop()
    post_meta.tables['reserved'].columns['time'].create()
    pre_meta.tables['waitlist'].columns['timestamp'].drop()
    post_meta.tables['waitlist'].columns['time'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reserved'].columns['timestamp'].create()
    post_meta.tables['reserved'].columns['time'].drop()
    pre_meta.tables['waitlist'].columns['timestamp'].create()
    post_meta.tables['waitlist'].columns['time'].drop()
