# DataPrep Assistant

A simple Python command-line tool that automates basic dataset cleaning tasks such as duplicate removal, missing value handling, and cleaning report generation.

## Features
- Detects and removes duplicate rows
- Identifies missing values column-wise
- Handles missing values intelligently
- Generates a cleaning report
- Supports CSV and Excel files

## Tech Stack
- Python
- Pandas
- OpenPyXL(for Excel file support)

## Output Files

The tool generates:

- datasetname_clean.csv → Cleaned dataset

- datasetname_duplicates.csv → Duplicate records (if present)

- datasetname_report.txt → Cleaning summary report

## Example Use Case

Useful for quick preprocessing of small to medium structured datasets before exploratory data analysis or machine learning workflows.

## Limitations

1. Uses fixed cleaning strategies (median / "Unknown")

2. Currently supports only CSV and Excel formats

3. Does not include advanced data validation or visualization
