import sql_config

#add a record to a database
#sql_config.add_one("Erick", "Agudelo","eagudelo@ryerson.ca")


#delete record from database
#sql_config.delete_one('8')


#add many records to a database
stuff = [
    ('Jerry','Stuff',"j@.ca"),
    ('Brenda','Raintree','raintree@.ca')
]
#sql_config.add_many(stuff)

#show all records in the database
sql_config.show_all()






