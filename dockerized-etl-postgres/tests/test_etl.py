
import pandas as pd
from etl.transform import transform_df

def test_transform_basic():
    df = pd.DataFrame({'patient_id':['A', None], 'age':['50','x'], 'visit_date':['2024-01-01','bad']})
    out = transform_df(df)
    assert 'patient_id' in out.columns
    assert out['patient_id'].notna().all()
    assert out['age'].dtype == int or out['age'].dtype == 'int64'
