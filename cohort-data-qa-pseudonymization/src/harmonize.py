
import pandas as pd
import yaml
import argparse

def load_map(mapfile):
    with open(mapfile,'r') as f:
        return yaml.safe_load(f)

def harmonize_csv(csvfile, mapfile, out):
    mapping = load_map(mapfile)
    df = pd.read_csv(csvfile)
    df = df.rename(columns=mapping.get('columns', {}))
    # units conversion example
    if 'date_of_birth' in df.columns:
        df['date_of_birth'] = pd.to_datetime(df['date_of_birth'], errors='coerce')
    df.to_csv(out, index=False)
    print('Harmonized saved to', out)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--map', required=True)
    parser.add_argument('--out', required=True)
    args = parser.parse_args()
    harmonize_csv(args.input, args.map, args.out)
