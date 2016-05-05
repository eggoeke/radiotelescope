from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
reserved = Table('reserved', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('telescope', VARCHAR(length=140)),
    Column('time', DATETIME),
    Column('user_id', INTEGER),
)

reserved_ashtarut = Table('reserved_ashtarut', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('time', DateTime),
    Column('user_id', Integer),
)

reserved_astarte = Table('reserved_astarte', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('time', DateTime),
    Column('user_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reserved'].drop()
    post_meta.tables['reserved_ashtarut'].create()
    post_meta.tables['reserved_astarte'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['reserved'].create()
    post_meta.tables['reserved_ashtarut'].drop()
    post_meta.tables['reserved_astarte'].drop()
