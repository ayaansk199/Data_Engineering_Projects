# Web Scraping Project - Top 50 Films

## Overview

This project involves web scraping the "100 Most Highly-Ranked Films" from the EverybodyWiki website. The goal is to extract relevant information such as average rank, film title, and release year from the web page and store it in a CSV file. Additionally, the project includes loading this data into an SQLite database for further analysis.

## Project Structure

- **webscrapping.py:** Python script for web scraping, data processing, and database loading.
- **top_50_films.csv:** Output CSV file containing the extracted data.
- **movie_database.db:** SQLite database file for storing the data.

## Prerequisites

- Python 3.x
- Required Python packages: pandas, requests, beautifulsoup4
- SQLite

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository

# Usage

Run the web scraping script:
python webscrapping.py
Check the output CSV file (top_50_films.csv) and the SQLite database file (movie_database.db) in the specified output directory.

# File Descriptions

webscrapping.py: The main script for web scraping, data processing, and database loading.
top_50_films.csv: CSV file containing the extracted data.
movie_database.db: SQLite database file for storing the data.

# Author

Ayaan Shaikh

# Acknowledgments

This project was created as part of the web scraping learning process.
