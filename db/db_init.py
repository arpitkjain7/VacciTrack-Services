import sqlite3

conn = sqlite3.connect("vaccitrack-backend.db")
c = conn.cursor()
# Create table - USERS
c.execute(
    """CREATE TABLE USERS
             ([username] text PRIMARY KEY,[name] text,[app_id] integer, [email_id] text, [timestamp] date)"""
)

conn.commit()
