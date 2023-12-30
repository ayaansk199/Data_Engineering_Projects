import pandas as pd
import numpy as np 
from bs4 import BeautifulSoup
import requests
import sqlite3
from datetime import datetime


# Defining known values

url = "https://web.archive.org/web/20230908091635 /https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attributes = ["Name" , "MC_USD_Billion"]
csv_path = "./Largest_banks_data.csv"
db_name = "Banks.db"
table_name = "Largest_banks"
exchange_data_rate_path = "file:///home/project/exchange_rate.csv"



# Task 1: Write a function log_progress()


# Task 1: Write a function log_progress()
def log_progress(message):
    timestamp_format = '%Y-%m-%d %H:%M:%S'  # Year-Month-Day Hour:Minute:Second
    timestamp = datetime.now().strftime(timestamp_format)
    
    log_entry = f"{timestamp} : {message}"
    
    with open("code_log.txt", "a") as log_file:
        log_file.write(log_entry + '\n')


#Task 2: Extract data from the given URL
def extract():
    df = pd.DataFrame(columns = table_attributes)

    html_page = requests.get(url)
    html_data = BeautifulSoup(html_page, "html.parser")

    tables = html_data.find_all("tbody")
    rows = tables[0].find_all('tr')
    col = rows.find_all("td")
    data_dict = {"Name": col[0].content[0],
                "MC_USD_Billion" : col[1].content[0]}
    df1 = pd.DataFrame(data_dict, index  = False)
    df = pd.concat([df, df1], ignore_index = True)
    return df


# Task 3: Transform the dataframe by adding columns for Market Capitalization in GBP, EUR and INR, rounded to 2 decimal places, based on the exchange rate information shared as a CSV file.

def transform(df):
    exchange_rate = pd.read_csv(exchange_data_rate_path)
     # Create a mapping dictionary for exchange rates
    exchange_rate_dict = dict(zip(exchange_rates['Currency'], exchange_rates[['GBP', 'EUR', 'INR']].values.tolist()))
    
    # Convert Market Capitalization to GBP, EUR, and INR
    df['MC_GBP_Billion'] = round(df['MC_USD_Billion'] * df['Currency'].map(exchange_rate_dict['GBP']), 2)
    df['MC_EUR_Billion'] = round(df['MC_USD_Billion'] * df['Currency'].map(exchange_rate_dict['EUR']), 2)
    df['MC_INR_Billion'] = round(df['MC_USD_Billion'] * df['Currency'].map(exchange_rate_dict['INR']), 2)
    
    return df[['Name', 'MC_USD_Billion', 'MC_GBP_Billion', 'MC_EUR_Billion', 'MC_INR_Billion']]

# Task 4: Load to CSV

def load_to_csv(df):
    df.to_csv(csv_path, index = False)
    log_progress("Data Loaded to CSV")

# Task 5: Load to SQL Database

def load_to_db(df):
    conn = sqlite3.connect("Bank.db")
    df.to_sql(table_name, conn, index = False, if_exists = 'replace')
    log_progress("Data loaded successfully in Database")

# Task 6: Run queries

def run_queries():
    conn = sqlite3.connect("Bank.db")
    query1 = pd.read_sql_query("SELECT * FROM Largest_banks;", conn)
    query2 = pd.read_sql_query("SELECT AVG(MC_GBP_Billion) FROM Largest_banks;", conn)
    query3 = pd.read_sql_query("SELECT Name from Largest_banks LIMIT 5;", conn)

if __name__ == "__main__":
    # Task 1
    log_progress("ETL Job Started")
    
    # Task 2
    log_progress("Extract phase Started")
    extracted_data = extract()
    log_progress("Extract phase Ended")
    
    # Task 3
    log_progress("Transform phase Started")
    transformed_data = transform(extracted_data)
    log_progress("Transform Phase Ended")
    
    # Task 4
    log_progress("Load to CSV phase Started")
    load_to_csv(transformed_data)
    log_progress("Load to CSV phase Ended")
    
    # Task 5
    log_progress("Load to SQL database phase Started")
    load_to_db(transformed_data)
    log_progress("Load to SQL database phase Ended")
    
    # Task 6
    log_progress("Run Queries phase Started")
    run_queries()
    log_progress("Run Queries phase Ended")
    
