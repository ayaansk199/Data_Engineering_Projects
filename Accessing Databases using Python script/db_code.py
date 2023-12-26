import sqlite3
import pandas as pd 

conn = sqlite3.connect("STAFF.db")
table_name = "INSTRUCTOR"
attribute_list = ["ID", "FNAME", "LNAME", "CITY", "CCODE"]

#Now, to read the CSV using Pandas, you use the read_csv() function. Since this CSV does not contain headers, you can use the keys of the attribute_dict dictionary as a list to assign headers to the data. For this, add the commands below to db_code.py.
file_path = '/home/project/INSTRUCTOR.csv'
df = pd.read_csv(file_path, names = attribute_list)


'''
The pandas library provides easy loading of its dataframes directly to the database. For this, you may use the to_sql() method of the dataframe object.
However, while you load the data for creating the table, you need to be careful if a table with the same name already exists in the database. If so, and it isn't required anymore, the tables should be replaced with the one you are loading here. You may also need to append some information to an existing table. For this purpose, to_sql() function uses the argument if_exists. The possible usage of if_exists is tabulated below
'''

df.to_sql(table_name, conn, if_exists = "replace", index = False)
print("Table is ready")


query = pd.read_sql("SELECT * FROM INSTRUCTOR", conn)
print(query)



#Appending new data
#Use the following statements to create the dataframe of the new data.
new_data = {"ID": [100], 
            "FNAME" :  ['John'],
            "LNAME" : ["Doe"],
            "CITY" : ["Paris"],
            "CCODE" : ["FR"]}


data_append = pd.DataFrame(new_data)

#Now use the following statement to append the data to the INSTRUCTOR table.

data_append.to_sql(table_name, conn, if_exists = "append", index = False )
print("Data appended successfully")

#Now, repeat the COUNT query. You will observe an increase by 1 in the output of the first COUNT query and the second one.
query = pd.read_sql("SELECT COUNT(*) FROM INSTRUCTOR", conn)
print(query)

conn.close()
