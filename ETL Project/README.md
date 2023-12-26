# Extract, Transform, and Load Data using Python

## Introduction
Extract, Transform and Load (ETL) operations are of extreme importance in the role of a Data engineer. 
A data engineer extracts data from multiple sources and different file formats, transforms the extracted data to predefined settings and then loads the data to a database for further processing. 

## Objectives
Read CSV, JSON, and XML file types.
Extract the required data from the different file types.
Transform data to the required format.
Save the transformed data in a ready-to-load format, which can be loaded into an RDBMS.


## How to Use
To execute this script successfully, follow these steps:

1. **Organize Your Files:**
   - Place all your data source files (CSV, JSON, XML) within the same folder where the Python script is located. This ensures easy access and extraction.

2. **Python Script Execution:**
   - Run the Python script in your preferred environment. Ensure you have the required libraries installed (Pandas, NumPy, etc.).

3. **ETL Process Overview:**
   - The script follows a typical ETL process: Extraction, Transformation, and Loading.

## Extraction Phase
   - The script iterates through all CSV, JSON, and XML files in the specified folder.
   - For each file type, a corresponding extraction function is called to read and load the data into a Pandas DataFrame.

## Transformation Phase
   - Height and weight values are transformed from inches/pounds to meters/kilograms, respectively.
   - The transformed data is then ready for further processing.

## Loading Phase
   - The transformed data is saved into a CSV file named "transformed_data.csv" in the same folder.

## Logging
   - The script logs each phase of the ETL process, including the start and end times of each phase, in a log file named "logfile.txt".

## Conclusion
This Python script serves as a foundation for automating ETL processes on diverse data sources. 

