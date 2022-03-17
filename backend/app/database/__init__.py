from flask import g  # g stands for global

import sqlite3

DATABASE = "user.db"


def get_db():
    db = getattr(g, "_database", None)
    if not db:
        db = g.database = sqlite3.connect(DATABASE)
    return db
