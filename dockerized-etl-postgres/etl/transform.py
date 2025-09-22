
import pandas as pd

def transform_df(df: pd.DataFrame) -> pd.DataFrame:
    # Basic cleaning and example QA
    df = df.copy()
    df.columns = [c.strip().lower() for c in df.columns]
    if 'age' in df.columns:
        df['age'] = pd.to_numeric(df['age'], errors='coerce').fillna(-1).astype(int)
    # Example: drop rows with missing patient_id
    df = df[df['patient_id'].notna()]
    # Example: ensure visit_date is datetime
    if 'visit_date' in df.columns:
        df['visit_date'] = pd.to_datetime(df['visit_date'], errors='coerce')
    return df
