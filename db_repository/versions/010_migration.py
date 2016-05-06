from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
reserved_ashtarut = Table('reserved_ashtarut', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('time', DATETIME),
    Column('user_id', INTEGER),
)

reserved_ashtarut = Table('reserved_ashtarut', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('starttime', DateTime),
    Column('endtime', DateTime),
    Column('user_id', Integer),
)

reserved_astarte = Table('reserved_astarte', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('time', DATETIME),
    Column('user_id', INTEGER),
)

reserved_astarte = Table('reserved_astarte', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('starttime', DateTime),
    Column('endtime', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reserved_ashtarut'].columns['time'].drop()
    post_meta.tables['reserved_ashtarut'].columns['endtime'].create()
    post_meta.tables['reserved_ashtarut'].columns['starttime'].create()
    pre_meta.tables['reserved_astarte'].columns['time'].drop()
    post_meta.tables['reserved_astarte'].columns['endtime'].create()
    post_meta.tables['reserved_astarte'].columns['starttime'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reserved_ashtarut'].columns['time'].create()
    post_meta.tables['reserved_ashtarut'].columns['endtime'].drop()
    post_meta.tables['reserved_ashtarut'].columns['starttime'].drop()
    pre_meta.tables['reserved_astarte'].columns['time'].create()
    post_meta.tables['reserved_astarte'].columns['endtime'].drop()
    post_meta.tables['reserved_astarte'].columns['starttime'].drop()
