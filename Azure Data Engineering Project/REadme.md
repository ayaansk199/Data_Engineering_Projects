# Azure Data Engineering Project
## Overview

Welcome to the Azure Data Engineering on Databricks Notebook! This notebook is designed to process error files stored in Azure Data Lake Storage, leveraging Azure Data Factory and Databricks for efficient data cleaning and analysis.

## Project Components

1. **Azure Blob Storage:**
   - Raw error files (`SingaporeErrorFile.csv` and `LuxembourgErrorFile.csv`) are uploaded here.

2. **Azure Data Factory Pipeline:**
   - Monitors Data Lake Storage for new files.
   - Orchestrates the movement of files to Data Lake.

3. **Data Lake Integration:**
   - Stores raw files in the input directory.
   - Facilitates seamless data transfer from Blob Storage.

4. **Databricks Notebook:**
   - PySpark or Pandas script for cleaning and processing error files.
   - Automated trigger upon new file arrival.

## Usage Instructions

1. **Upload Files to Azure Blob Storage:**
   - Upload `SingaporeErrorFile_EI.csv` and `SingaporeErrorFile_ER.csv` to Azure Blob Storage.

2. **Execute Azure Data Factory Pipeline:**
   - Ensure the Data Factory pipeline is configured to trigger upon new file arrival in Data Lake.
   - Monitor the execution in the Azure portal.

3. **Data Processing with Databricks:**
   - Open this notebook in Databricks.
   - Execute each cell to perform data cleaning and analysis.
   - Ensure that the notebook is configured for automatic triggering upon new file arrival.

4. **Output:**
   - Cleansed data is stored in the Data Lake output directory with filenames appended with the current date.

## Important Notes

- The notebook is designed to handle error files with specific structures. Ensure that the structure of incoming files aligns with the expected format.
- Customize the notebook as needed based on specific project requirements.

## Authors

- Ayaan Shaikh

## Changelog

- Version 1.0 (2024-02-03): Initial version of the Databricks notebook.

Feel free to reach out for any questions or assistance!

---

**Note:** This README serves as a guideline. Customize it further based on specific project details and updates.

