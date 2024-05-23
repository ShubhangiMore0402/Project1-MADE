import pandas as pd
from sqlalchemy import create_engine, TEXT, FLOAT, BIGINT
import numpy as np
import os

def drop_columns(df, col_list):
    """
    This will remove specified columns from a pandas DataFrame.

    Parameters:
    df (pd.DataFrame): This is the DataFrame from which specified columns are to be removed.
    col_list (list): A list of strings shows the names of the columns which are to be removed.

    Returns:
    pd.DataFrame: It returns the modified DataFrame with the specified columns which are removed.
    """

    # Dropping the specified columns from the DataFrame
    df.drop(col_list, axis=1, inplace=True)

    return df

def rename_columns(df, col_dict):
    """
    Columns of a pandas DataFrame are renamed based on a provided dictionary mapping.

    Parameters:
    df (pd.DataFrame): These are the DataFrame whose columns are to be renamed.
    col_dict (dict): A dictionary mapping the current column names to the new column names.

    Returns:
    pd.DataFrame: The DataFrame with columns renamed as it is specified in the col_dict.
    """

    # Renaming columns of the DataFrame as per the provided dictionary mapping
    df.rename(columns=col_dict, inplace=True)

    return df

def fix_date_format(df, col_list):
    """
    Arranging the format of date columns the DataFrame.

    Parameters:
    df (pd.DataFrame): The DataFrame which contains the date columns which are to be formatted.
    col_list (list): A list of column names (strings) in the DataFrame that contains date information.

    Returns:
    pd.DataFrame: The DataFrame with adjusted date formats in the specified columns.
    """

    # Iterating over each column in the provided column list
    for col in col_list:
        df[col] = pd.to_datetime(df[col], format='%Y-%m-%d %H:%M:%S')
        df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M')   
    return df

def transform_df_data(df):

    data_col_del = ['Data Source', 'Data Estimated', 'Data Estimation Method']

				
    # Data dictionary for renaming the columns
    data_col_rename = {
        'Datetime (UTC)': 'date_and_time',
        'Country': 'country',
        'Zone Name': 'zone_name',
        'Zone Id': 'zone_id',
        'Carbon Intensity gCO₂eq/kWh (direct)': 'direct_carbon_intensity',
        'Carbon Intensity gCO₂eq/kWh (LCA)': 'lca_carbon_intensity',
        'Low Carbon Percentage': 'low_carbon_percentage',
        'Renewable Percentage': 'renewable_percentage'
    }

    # Columns containing date information
    date_columns = ['date_and_time']

     # Dropping unnecessary columns
    df = drop_columns(df, data_col_del)

    # Renaming columns for clarity
    df = rename_columns(df, data_col_rename)

    # Fixing the date format
    df = fix_date_format(df, date_columns)

    columns_neg_val = ['direct_carbon_intensity', 'lca_carbon_intensity', 'low_carbon_percentage', 'renewable_percentage']
    df[columns_neg_val] = df[columns_neg_val].map(lambda x: abs(x) if x < 0 else x)

    return df

def get_source_data(path, delimiter):
    """
    Reads data from the mentioned file path into the DataFrame.

    Parameters:
    path (str): The file path from which the data is to be read.
    delimiter (str): Indicates the delimiter used in the file (e.g., ',', ';', '\t', etc.).

    Returns:
    pd.DataFrame: A DataFrame which contains the imported data.
    """
    # Using pandas package to read data from the specified file path and the given delimiter
    df = pd.read_csv(path, delimiter=delimiter)
    return df

def write_to_target(df, engine, table_name):
    """
    Writes a pandas DataFrame to a SQL table.

    Parameters:
    df (pd.DataFrame): The DataFrame to be written to the SQL table.
    engine: The SQLAlchemy engine instance used to connect to the database.
    table_name (str): The name of the target table in the SQL database where the data will be written.

    Note: Ensure that the connection specified by 'engine' is open and valid before calling this function.
    """

    # Writing the DataFrame to the specified SQL table without including the DataFrame's index
    df.to_sql(table_name, engine, if_exists='replace', index=False)


def automated_data_pipeline(details):
    germany_df = get_source_data(details['germany_data']['source'], details['germany_data']['delimiter'])
    britain_df = get_source_data(details['britain_data']['source'], details['britain_data']['delimiter'])

    germany_df = transform_df_data(germany_df)
    britain_df = transform_df_data(britain_df)

    engine = create_engine(f"sqlite:///{details['target_db_path']}\\{details['target_db_name']}.db")

    write_to_target(germany_df, engine, details['germany_data']['target_table'])
    write_to_target(britain_df, engine, details['britain_data']['target_table'])

if __name__ == '__main__':
    src_tgt_details = {
        'germany_data' : {
            'source' : "https://raw.githubusercontent.com/ShubhangiMore0402/Project1-MADE/main/data/DE_2022_hourly.csv",
            'delimiter' : ',',
            'target_table' : 'germany_data'
        },
        'britain_data' : {
            'source' : "https://raw.githubusercontent.com/ShubhangiMore0402/Project1-MADE/main/data/GB_2022_hourly.csv",
            'delimiter' : ',',
            'target_table' : 'britain_data'
        },
        'target_db_path' : '../data',        
        'target_db_name' : 'made-project_new'
    }

    germany_df = get_source_data(src_tgt_details['germany_data']['source'], src_tgt_details['germany_data']['delimiter'])
    britain_df = get_source_data(src_tgt_details['britain_data']['source'], src_tgt_details['britain_data']['delimiter'])
    
    germany_df = transform_df_data(germany_df)
    britain_df = transform_df_data(britain_df)

    # Ensure directory exists
    os.makedirs(src_tgt_details['target_db_path'], exist_ok=True)

    engine = create_engine(f"sqlite:///{src_tgt_details['target_db_path']}//{src_tgt_details['target_db_name']}.db")
    write_to_target(germany_df, engine, src_tgt_details['germany_data']['target_table'])
    write_to_target(britain_df, engine, src_tgt_details['britain_data']['target_table'])

    engine.dispose()
