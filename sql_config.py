import sqlite3

# SQLite Data types
# real, float, text, Blobs (binary large objects), Null




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


#query the DATABASE and Return all Records
def show_all():

    # conn = sqlite3.connect(':memory:') - would disappear as soon as the program closes
    conn = sqlite3.connect('OurDatabase.db')

    # create cursor
    c = conn.cursor()

    c.execute("SELECT ROWID, * FROM customers")
    items = c.fetchall()

    for item in items:
        print(item)

    # commit our command
    conn.commit()

    # close our connection
    conn.close()


# New record to Database
def add_one(first,last,email):
    conn = sqlite3.connect('OurDatabase.db')
    c = conn.cursor()
    c.execute("INSERT INTO customers VALUES(?,?,?)",(first, last, email))
    conn.commit()
    conn.close()


def delete_one(id):
    conn = sqlite3.connect('OurDatabase.db')
    c = conn.cursor()
    c.execute("DELETE from customers WHERE rowid = (?)", id)
    conn.commit()
    conn.close()



def add_many(list):
    conn = sqlite3.connect('OurDatabase.db')
    c = conn.cursor()
    c.executemany("INSERT INTO customers VALUES(?,?,?)",(list))
    conn.commit()
    conn.close()






