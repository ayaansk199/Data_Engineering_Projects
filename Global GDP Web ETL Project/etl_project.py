## Importing the required libraries
import requests
import sqlite3
from bs4 import BeautifulSoup
import pandas as pd 
from datetime import datetime
import numpy as np 

#Defining known valuesdefining known values
db_name = "World_Economies.db"
table_name = "Countries_by_GDP"
table_attributes = ["Country", "GDP_USD_millions"]
csv_path = "./Countries_by_GDP.csv"
url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"

#Task 1: Exctract - Write a data extraction function to retrieve the relevant information from the required URL.
def extract(url, table_attribs):
    page = requests.get(url).text
    data = BeautifulSoup(page,'html.parser')
    df = pd.DataFrame(columns=table_attribs)
    tables = data.find_all('tbody')
    rows = tables[2].find_all('tr')
    for row in rows:
        col = row.find_all('td')
        if len(col)!=0:
            if col[0].find('a') is not None and '—' not in col[2]:
                data_dict = {"Country": col[0].a.contents[0],
                             "GDP_USD_millions": col[2].contents[0]}
                df1 = pd.DataFrame(data_dict, index=[0])
                df = pd.concat([df,df1], ignore_index=True)
    return df


#Task 2: Transforming - Transform the available GDP information into 'Billion USD' from 'Million USD'
def transform(df):
    GDP_list = df["GDP_USD_millions"].to_list()
    GDP_list = [float("".join(x.split(","))) for x in GDP_list] 
    GDP_list = [np.round(x/1000,2) for x in GDP_list ]
    df["GDP_USD_millions"] = GDP_list
    df = df.rename(columns =  {"GDP_USD_millions" : "GDP_USD_billions"})

    return df 


#Task 3: Loading data

def load_csv(df, csv_path):
    df.to_csv(csv_path)

def load_to_db(df, sql_connection, table_name):
    sql_connection = sqlite3.connect(db_name)
    df.to_sql(table_name, sql_connection, if_exists = 'replace', index = True)

# Task 4:  Querying the database table 

def run_query(query, sql_connection):
    print(query)
    query_output = pd.read_sql(query, sql_connection)
    print(query_output)

# Task 5: Logging progress

def log_progress(message):
    timestamp_format = "%Y-%m-%d-%H:%M:%S" # Year-Monthname-Day-Hour-Minute-Second 
    now = datetime.now() #Get the current time
    timestamp = now.strftime(timestamp_format)
    with open("./etl_project_log.txt", "a") as f:
        f.write(timestamp + " : " + message + "\n")


log_progress("Preliminaries complete. Initiating the ETL Process")

df = extract(url, table_attributes)

log_progress("Data Extraction Completed")

df = transform(df)

log_progress("Data Transformation Completed")

load_csv(df, csv_path)

log_progress("Data saved as CSV file")

sql_connection = sqlite3.connect(db_name)

load_to_db(df, sql_connection, table_name)

log_progress(f"Data loaded to Database as table name {table_name} ...Running the query")

query = f"SELECT * FROM {table_name} WHERE  GDP_USD_billions >= 100"

run_query(query, sql_connection)

log_progress("Process complete")

sql_connection.close()
    

