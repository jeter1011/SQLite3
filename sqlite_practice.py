import sql_config as slp


conn = slp.conn
c = slp.c

#many_customers = [('Wes','Brown','wes@code.ca'),
#                  ('Steph','Jea','sj@code.ca'),
#                  ('Dan','Pas','Dan@code.ca')
#                  ]

#  c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

#c.fetchone()
#c.fetchmany(#)
#c.fetchall


#Update Records

#c.execute("""UPDATE customers SET first_name = 'John'
#   WHERE ROWID = 1
#""")

# DELETING stuff
#c.execute("DELETE from customers WHERE ROWID =6 ")


c.execute("SELECT ROWID, * FROM customers WHERE last_name LIKE 'Br%' or first_name = 'Mary'")

items = c.fetchall()

for item in items:
   print(item)



conn.commit()
conn.close()




