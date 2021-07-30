import pandas as pd
import sqlalchemy
import sqlite3

# SQLite Data types
# real, float, text, Blobs (binary large objects), Null


# conn = sqlite3.connect(':memory:') - would disappear as soon as the program closes
conn = sqlite3.connect('OurDatabase.db')

# create cursor
c = conn.cursor()

# create table

#    c.execute("""CREATE TABLE customers (
#            first_name TEXT,
#         last_name TEXT,
#         email TEXT
#        )""")


# Deleting Table
# c.execute("DROP TABLE customers")

# commit our command
# c.commit()

# close our connection
#c.close()
