
import os
from sqlalchemy import create_engine

def get_db_url():
    return os.environ.get('DATABASE_URL', 'postgresql://etl_user:etl_pass@localhost:5432/etl_db')

def write_df_to_db(df, table_name, db_url=None):
    if db_url is None:
        db_url = get_db_url()
    engine = create_engine(db_url)
    df.to_sql(table_name, engine, if_exists='append', index=False)
