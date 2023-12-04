import mysql.connector
import time
from datetime import datetime

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "root",
    database = "test_1"
)

now = datetime.now()

mycursor = db.cursor()
print(db)
print("-----------------")




# Database creation
#mycursor.execute("CREATE DATABASE test_1")




# Table creation
#mycursor.execute("CREATE TABLE person (name VARCHAR(50), age smallint UNSIGNED, personID int PRIMARY KEY AUTO_INCREMENT)")
#mycursor.execute("CREATE TABLE test_2 (name VARCHAR(50) NOT NULL, created datetime NOT NULL, gender ENUM ('M', 'F', 'O') NOT NULL, id int PRIMARY KEY AUTO_INCREMENT NOT NULL)")
#mycursor.execute("CREATE TABLE work1 (gas int UNSIGNED, ht int UNSIGNED, lt int UNSIGNED, entrydate VARCHAR(50), entryID int PRIMARY KEY AUTO_INCREMENT)")
#print("done")




# Display table row and column alocations, definitions
#mycursor.execute("DESCRIBE work1")
#for x in mycursor:
#    print(x)




# Importing Data into Database
#mycursor.execute("INSERT INTO person (name, age) VALUES (%s,%s)", ("Branislav", 43))
#mycursor.execute("INSERT INTO test_2 (name, created, gender) VALUES (%s,%s,%s)", ("Actor", datetime.now(), "O"))
#db.commit()
#print("done")


#mycursor.execute("SELECT * FROM work1")
#result = mycursor.fetchall()
#for row in result:
    #print(row)

#print("-------------------------------------------------------------")
#time.sleep(1)




# Table Query
#mycursor.execute("SELECT * FROM test_2 WHERE gender = 'M' ORDER BY id DESC")
#for x in mycursor:
#    print(x)

#update_db = "UPDATE test_2 SET (name, created, gender) = ('Aktorka', now, "F") WHERE gender = 'O'"
#update_db = "UPDATE test_2 SET name = 'Aktorka', created = NOW(), gender = 'F' WHERE gender = 'O'"

#update_db = "UPDATE work1 SET entrydate_month = 'Aktorka', created = NOW(), gender = 'F' WHERE gender = 'O'"


#mycursor.execute(update_db)
#db.commit()


# Adding Rows to existent table
#mycursor.execute("ALTER TABLE work1 \ ")







# Specify the table and columns to add
table_name = "work1"
#f"UPDATE {table_name} SET year_smallint = SUBSTRING(entrydate_string, 1, 4) WHERE entrydate_string LIKE '____%may'"

#query = f"UPDATE {table_name} SET entrydate_month = '12' WHERE entrydate LIKE '_____December'"


#new_columns = [
    #("entrydate_month", "smallint"),  # Adjust data type and size as needed
    #("entrydate_year", "smallint"),
    # Add more columns as needed
#]

# Build the SQL query to add columns
#for column, data_type in new_columns:
    #alter_query = f"ALTER TABLE {table_name} ADD COLUMN {column} {data_type}"
    #mycursor.execute(alter_query)

#mycursor.execute(query)
#db.commit()
# Commit the changes to the database
#db.commit()


table_name = "work1"
condition_year = "entrydate_year"
condition_month = "entrydate_month"
date_year_var = 2023
date_month_var = "03"

current_month_query = f"SELECT gas FROM {table_name} WHERE {condition_year} = %s AND {condition_month} = %s"
mycursor.execute(current_month_query, (date_year_var, date_month_var))

single_cell_data = mycursor.fetchone()
print(date_year_var, date_month_var)
print(single_cell_data)