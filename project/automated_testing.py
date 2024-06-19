import pandas as pd
import sqlite3
import sys
import os
import numpy as np


def read_sql_table(db_path, table_name):
    # Check if the database file exists
    if not os.path.exists(db_path):
        print(f"Error: Database file '{db_path}' does not exist.")
        return pd.DataFrame()

    try:
        # Establish connection to the SQLite database
        conn = sqlite3.connect(db_path)

        # Check if the table exists in the database
        cursor = conn.cursor()
        cursor.execute(f"SELECT name FROM sqlite_master WHERE type='table' AND name='{table_name}'")
        table_exists = cursor.fetchone()

        if not table_exists:
            print(f"Error: Table '{table_name}' does not exist in the database.")
            return pd.DataFrame()

        # Read the SQL table into a pandas DataFrame
        query = f"SELECT * FROM {table_name}"
        df = pd.read_sql_query(query, conn)

        # Close the database connection
        conn.close()

        return df

    except Exception as e:
        print(f"Error occurred while reading SQL table: {e}")
        return pd.DataFrame()

def check_data_exists(data, data_name):
    if not data.empty:
        print(f"{data_name} data output file exists and contains data.")
        return True
    else:
        print(f"{data_name} data output file does not contain any data.")
        return False
    
def remove_rows_with_nulls(df):
    # Remove rows with any null values
    cleaned_df = df.dropna()
    return cleaned_df

if __name__ == '__main__':
    src_tgt_details = {
        'world_data' : {
            'target_table' : 'world_data'
        },
        'europe_data' : {
            'target_table' : 'europe_data'
        },
        'target_db_path' : '.\\data',        
        'target_db_name' : 'made-project_new'
    }

    db_path = f"{src_tgt_details['target_db_path']}//{src_tgt_details['target_db_name']}.db"
    world_data = read_sql_table(db_path, src_tgt_details['world_data']['target_table'])
    europe_data = read_sql_table(db_path, src_tgt_details['europe_data']['target_table'])
    if check_data_exists(world_data, "World") and check_data_exists(europe_data, "Europe"):
        print("Removing rows with any null values")
        world_data = remove_rows_with_nulls(world_data)
        europe_data = remove_rows_with_nulls(europe_data)
        print("All tests passed.")
    else:
        print("Tests failed")
