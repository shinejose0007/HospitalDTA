
import os
from transform import transform_df
from db import write_df_to_db, get_db_url
import pandas as pd

def main():
    db_url = get_db_url()
    print('Using DB URL:', db_url)
    df = pd.read_csv('etl/sample_data.csv')
    print('Loaded sample data rows:', len(df))
    df_clean = transform_df(df)
    write_df_to_db(df_clean, 'cohort', db_url)
    print('ETL finished.')

if __name__ == '__main__':
    main()
