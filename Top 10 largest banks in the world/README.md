# Banks Data ETL Project

This project involves extracting data from a Wikipedia page listing the largest banks, transforming the data to include market capitalization in different currencies, and loading the results into a CSV file and SQLite database.

## Project Structure

- `banks_project.py`: Python script containing the main ETL (Extract, Transform, Load) process.
- `Largest_banks_data.csv`: CSV file containing the transformed data.
- `Banks.db`: SQLite database for storing the transformed data.
- `exchange_rate.csv`: CSV file containing exchange rates for different currencies.
- `code_log.txt`: Log file to track progress and messages during the ETL process.

## Requirements

- Python 3.11
- Pandas
- BeautifulSoup
- Requests

## Setup

1. **Clone the repository:**

   ```bash
   git clone <repository_url>
   cd <repository_directory>


# Project Details

## Extract
The script extracts data from a Wikipedia page that lists the largest banks. It uses BeautifulSoup to parse the HTML content and retrieve relevant information.

## Transform
The extracted data is transformed by adding columns for market capitalization in GBP, EUR, and INR, based on exchange rates provided in the exchange_rate.csv file.

## Load
The transformed data is loaded into a CSV file (Largest_banks_data.csv) and an SQLite database (Banks.db).
