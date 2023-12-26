## Project Overview
This project involves creating a SQLite database named `STAFF.db`, a table named `INSTRUCTOR`, and loading data into it from a CSV file named `INSTRUCTOR.csv`. The Pandas library is used for data manipulation, and the code ensures that existing tables are replaced if necessary.

## Project Structure
- **`db_code.py`**: Python script for database operations.
- **`INSTRUCTOR.csv`**: CSV file containing data to be loaded into the database.


## Instructions
1. Ensure you have SQLite and Pandas installed.
2. Run `db_code.py` to create the database, table, and load data.
3. Check the output and observe the table creation and data loading.
4. To append new data, modify the `new_data` dictionary in the script.
5. Re-run the script to see the data appended and check the updated count.

## Dependencies
- Python 3.x
- Pandas
- SQLite

## Run the final code
```bash
python db_code.py