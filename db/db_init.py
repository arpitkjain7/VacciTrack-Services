import sqlite3

conn = sqlite3.connect("vaccitrack-backend.db")
c = conn.cursor()
# Create table - USERS
c.execute(
    """CREATE TABLE USERS
             ([username] text PRIMARY KEY,[name] text,[app_id] text, [password] text,[email_id] text, [timestamp] date)"""
)
c.execute(
    """CREATE TABLE ADMIN
             ([username] text PRIMARY KEY,[name] text,[password] text, [timestamp] date)"""
)
c.execute(
    """ INSERT INTO USERS(username,name,app_id,email_id,password,timestamp)
              VALUES('admin_user','admin',123,'admin@vaccitrack.com','admin@123',123) """
)
conn.commit()
