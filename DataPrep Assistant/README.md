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

## Working

The cleaning pipeline performs the following steps:

1. Dataset Loading

Automatically detects file type (CSV or Excel)

2. Duplicate Handling

Identifies duplicate rows

Saves duplicate records in a separate file

Removes duplicates from main dataset

3. Missing Value Handling

Drops rows where ID-related columns contain missing values

Fills numeric columns using median values

Fills categorical columns with "Unknown"

4. Report Generation

Creates a text report summarizing:

Initial and final row count

Duplicate records removed

Rows dropped due to missing IDs

Column-wise missing value summary

## Purpose
This project was built to strengthen foundational data preprocessing and automation skills.

