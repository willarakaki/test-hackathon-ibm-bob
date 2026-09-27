import os
import sqlite3
from contextlib import contextmanager
from typing import Generator

# Clean configuration loaded from environment variables
DB_PATH = os.getenv("DB_PATH", "app.db")

@contextmanager
def get_db_connection() -> Generator[sqlite3.Connection, None, None]:
    """Provides a transactional scope around a series of operations."""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def initialize_db() -> None:
    """Initialize the database schema."""
    with get_db_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT UNIQUE NOT NULL
            )
        """)
        conn.commit()
