# Import dependencies
import pandas as pd
import openpyxl
import xlrd
import os


def load_data(file_path):
    """
    Load dataset based on file type.
    Supports CSV and Excel files.
    """

    if file_path.endswith(".csv"):
        print("Dataset type: CSV")
        return pd.read_csv(file_path, encoding_errors="ignore")

    elif file_path.endswith(".xlsx"):
        print("Dataset type: Excel")
        return pd.read_excel(file_path)

    else:
        print("Unsupported file format.")
        return None


def remove_duplicates(df, data_name):
    # Identify and remove duplicate rows.
    # Saves duplicate rows separately.

    duplicates = df.duplicated()
    total_duplicates = duplicates.sum()

    print(f"Total duplicate records in the dataset: {total_duplicates}")

    if total_duplicates > 0:
        duplicate_rows = df[duplicates]
        duplicate_rows.to_csv(f"{data_name}_duplicates.csv", index=False)

    cleaned_df = df.drop_duplicates()

    return cleaned_df, total_duplicates


def handle_missing_values(df):
    """
    Handle missing values:
    - Drop rows where ID columns have missing values
    - Fill numeric columns with median
    - Fill categorical columns with 'Unknown'
    """

    original_rows = df.shape[0]

    # Identify ID columns
    id_columns = [col for col in df.columns if "id" in col.lower()]

    # Drop rows where ID columns have missing values
    if id_columns:
        df = df.dropna(subset=id_columns)

    rows_after_id_drop = df.shape[0]
    rows_dropped = original_rows - rows_after_id_drop

    # Fill remaining missing values
    for col in df.columns:

        if col in id_columns:
            continue

        if pd.api.types.is_numeric_dtype(df[col]):
            df[col] = df[col].fillna(df[col].median())

        else:
            df[col] = df[col].fillna("Unknown")

    total_missing_after = df.isnull().sum().sum()

    return df, rows_dropped, total_missing_after


def save_clean_data(df, data_name):

    output_file = f"{data_name}_clean.csv"
    df.to_csv(output_file, index=False)
    print(f"Cleaned dataset saved as {output_file}")



def generate_report(data_name, df, initial_rows, final_rows, duplicates_removed, rows_dropped):
    """
    Generate detailed cleaning summary report.
    """

    total_missing = df.isnull().sum().sum()
    missing_by_column = df.isnull().sum()

    report_text = f"""
DATA CLEANING REPORT


DATASET SUMMARY
Initial Rows: {initial_rows}
Final Rows: {final_rows}
Total Columns: {df.shape[1]}

CLEANING ACTIONS
Duplicates Removed: {duplicates_removed}
Rows Dropped Due to Missing ID: {rows_dropped}

MISSING VALUE SUMMARY
Total Missing Values Remaining: {total_missing}

Missing Values By Column:
"""

    # Add column-wise missing values
    for col, val in missing_by_column.items():
        report_text += f"{col}: {val}\n"

    with open(f"{data_name}_report.txt", "w") as file:
        file.write(report_text)

    print("Detailed cleaning report generated.")


def data_cleaning_application(file_path, data_name):
    """
    Main pipeline to run data cleaning.
    """

    df = load_data(file_path)

    if df is None:
        return

    initial_rows = df.shape[0]

    print(f"Dataset contains {df.shape[0]} rows")
    print(f"Dataset contains {df.shape[1]} columns")

    # Show missing values BEFORE cleaning
    total_missing_vals = df.isnull().sum().sum()
    missing_val_col = df.isnull().sum()

    print(f"\nNo of missing values in the dataset: {total_missing_vals}")
    print("\nMissing values by columns:")
    print(missing_val_col)

    # Remove duplicates
    df, duplicates_removed = remove_duplicates(df, data_name)

    # Handle missing values
    df, rows_dropped, missing_remaining = handle_missing_values(df)

    final_rows = df.shape[0]

    print("\nCleaning Completed!")
    print(f"Final dataset rows: {final_rows}")
    print(f"Remaining missing values: {missing_remaining}")

    # Save cleaned dataset
    save_clean_data(df, data_name)

    # Generate report
    generate_report(data_name, df, initial_rows, final_rows, duplicates_removed, rows_dropped)


if __name__ == "__main__":

    while True:
        file_path = input("Enter dataset file path: ")

        if os.path.exists(file_path):
            break
        else:
            print("Invalid path. Please try again.")

    data_name = input("Enter dataset name: ")

    data_cleaning_application(file_path, data_name)
