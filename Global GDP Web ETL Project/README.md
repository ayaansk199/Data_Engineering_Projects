# Overview
GlobalGDP WebETL Project is a data pipeline that extracts GDP information from a Wikipedia page using web scraping, transforms the data, and loads it into a SQLite database.

# Project Structure
- etl_project.py: Main script containing the ETL process, including web scraping.
- World_Economies.db: SQLite database to store the transformed data.
- Countries_by_GDP.csv: CSV file for intermediate data storage.
- etl_project_log.txt: Log file to track progress.
 

# Web Scraping
The project uses web scraping to extract GDP information from the [Wikipedia page](https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29).


# Log
Check etl_project_log.txt for the log of the ETL process.

# Author
Ayaan Shaikh