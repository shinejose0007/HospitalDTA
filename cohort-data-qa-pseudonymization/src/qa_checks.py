
import pandas as pd
import json

def run_checks(df):
    report = {}
    report['n_rows'] = len(df)
    report['missing'] = df.isna().sum().to_dict()
    report['duplicates'] = df.duplicated().sum()
    return report

if __name__ == '__main__':
    df = pd.read_csv('data/cohort_a.csv')
    print(run_checks(df))
