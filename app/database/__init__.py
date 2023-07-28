import os
import click
from flask.cli import with_appcontext
from flask import g
from datetime import datetime
from sqlalchemy import (
    create_engine,
    MetaData,
    Connection,
    Table,
    Column,
    Integer,
    Text,
    DateTime,
    ForeignKey,
    CheckConstraint,
    String
)


engine = create_engine(os.getenv("DATABASE_URL"))

metadata = MetaData()

users = Table(
    "users",
    metadata,
    Column("id", Integer(), primary_key=True, index=True),
    Column("name", Text(), index=True),
    Column("email", Text(), unique=True, index=True),
    Column("profile_pic", Text(), nullable=True),
)

projects = Table(
    "projects",
    metadata,
    Column("id", Integer(), primary_key=True, index=True),
    Column("name", Text()),
    Column("description", Text()),
    Column("owner", Integer(), ForeignKey("users.id"), index=True),
    Column("created_at", DateTime(), default=datetime.now),
)

endpoint = Table(
    "endpoint",
    metadata,
    Column("id", Integer(), primary_key=True, index=True),
    Column("project_id", Integer(), ForeignKey("users.id"), index=True),
    Column("method", String(6)),
    Column("url", Text()),
    Column("name", Text()),
    Column("description", Text()),
    Column("created_at", DateTime(), default=datetime.now),
    CheckConstraint("method IN ('GET', 'POST', 'PATCH', 'PUT', 'DELETE')", name='cc_method')
)

def get_db() -> Connection:
    if "db" not in g:
        g.db = engine.connect()
    return g.db


def close_db(e=None):
    db = g.pop("db", None)

    if db is not None:
        db.close()


def init_db():
    metadata.create_all(bind=engine)


@click.command("init-db")
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo("Initialized the database.")


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)
