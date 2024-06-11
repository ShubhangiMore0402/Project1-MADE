import pandas as pd
from sqlalchemy import create_engine, TEXT, FLOAT, BIGINT
import numpy as np
import os
import requests
import io


def drop_columns(df, col_list):
    
    existing_cols = [col for col in col_list if col in df.columns]
    # Dropping the specified columns from the DataFrame
    df.drop(existing_cols, axis=1, inplace=True)

    return df

def rename_columns(df, col_dict):
  
    # Renaming columns of the DataFrame as per the provided dictionary mapping
    df.rename(columns=col_dict, inplace=True)

    return df

def fix_date_format(df, col_list):

    # Iterating over each column in the provided column list
    for col in col_list:
        df[col] = pd.to_datetime(df[col], format='%Y-%m-%d %H:%M:%S')
        df[col] = df[col].dt.strftime('%Y-%m-%d %H:%M')   
    return df

def transpose_data(df):
    if 'YEAR' in df.columns or 'VALUE'  in df.columns:
         col_list = df.columns.values.tolist()
         existing_cols = [col for col in col_list if col in df.columns and col not in ['YEAR', 'VALUE']]
         pivoted_df = df.pivot(index=existing_cols, columns="YEAR", values="VALUE").reset_index()
         return pivoted_df
    else:
        return df


def transform_df_data(df):

    data_col_del = [
    '1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977', '1978', '1979', 
    '1980', '1981', '1982', '1983', '1984', '1985', '1986', '1987', '1988', '1989', 
    '1990', '1991', '1992', '1993', '1994', '1995', '1996', '1997', '1998', '1999', 
    '2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', 
    '2010', '2011', '2012', 'LEVEL_ID', 'TERRITORY_ID', 'DATE'
     ]
    data_col_rename = {
        2019: 'Year_2019',
        2020: 'Year_2020',
        2021: 'Year_2021',
        2022: 'Year_2022'
    }	
     # Dropping unnecessary columns
    df = drop_columns(df, data_col_del)
    df = transpose_data(df)
    df = rename_columns(df, data_col_rename)
    return df

def get_source_data(path, delimiter):
    # Use io.StringIO to simulate a file object
    response = requests.get(path)
    csv_file = io.StringIO(response.text)

# Read the CSV file and filter out lines ending with ",,,,,,,,"
    filtered_lines = [line for line in csv_file if not line.strip().endswith(",,,,,,,")]

# Join the filtered lines into a single string
    filtered_csv_data = "".join(filtered_lines)

# Use pandas to read the filtered CSV data into a DataFrame
    df = pd.read_csv(io.StringIO(filtered_csv_data), delimiter=delimiter)   
    # Using pandas to read data from the specified file path with the given delimiter
    # df = pd.read_csv(path, delimiter=delimiter)
    return df

def write_to_target(df, engine, table_name):
   
    # Writing the DataFrame to the specified SQL table without including the DataFrame's index
    df.to_sql(table_name, engine, if_exists='replace', index=False)


def automated_data_pipeline(details):
    world_df = get_source_data(details['world_data']['source'], details['world_data']['delimiter'])
    europe_df = get_source_data(details['europe_data']['source'], details['europe_data']['delimiter'])

    world_df = transform_df_data(world_df)
    europe_df = transform_df_data(europe_df)

    engine = create_engine(f"sqlite:///{details['target_db_path']}\\{details['target_db_name']}.db")

    write_to_target(world_df, engine, details['world_data']['target_table'])
    write_to_target(europe_df, engine, details['europe_data']['target_table'])

if __name__ == '__main__':
    src_tgt_details = {
        'world_data' : {
            'source' : "https://jeodpp.jrc.ec.europa.eu/ftp/jrc-opendata/EDGAR/datasets/v432_FT2016/EDGARv432_FT2016_CO2_per_GDP_emissions_1970-2016.csv",
            'delimiter' : ',',
            'target_table' : 'world_data'
        },
        'europe_data' : {
            'source' : "https://urban.jrc.ec.europa.eu/api/udp/v2/en/data/?databrick_id=739&nutslevel=0&ts=TOURISM&nutsversion=-1&mpx=1&nutslevel=9&format=csv",
            'delimiter' : ',',
            'target_table' : 'europe_data'
        },
        'target_db_path' : '../data',        
        'target_db_name' : 'made-project_new'
    }

    world_df = get_source_data(src_tgt_details['world_data']['source'], src_tgt_details['world_data']['delimiter'])
    europe_df = get_source_data(src_tgt_details['europe_data']['source'], src_tgt_details['europe_data']['delimiter'])
    
    world_df = transform_df_data(world_df)
    europe_df = transform_df_data(europe_df)

    # Ensure directory exists
    os.makedirs(src_tgt_details['target_db_path'], exist_ok=True)

    engine = create_engine(f"sqlite:///{src_tgt_details['target_db_path']}//{src_tgt_details['target_db_name']}.db")
    write_to_target(world_df, engine, src_tgt_details['world_data']['target_table'])
    write_to_target(europe_df, engine, src_tgt_details['europe_data']['target_table'])

    engine.dispose()

