
import hashlib
import pandas as pd

def pseudonymize_id(idval, salt='somesalt'):
    return hashlib.sha256((salt + str(idval)).encode('utf-8')).hexdigest()

if __name__ == '__main__':
    df = pd.read_csv('data/cohort_a.csv')
    df['pseud_id'] = df['id'].apply(lambda x: pseudonymize_id(x))
    df[['id','pseud_id']].to_csv('pseud_map.csv', index=False)
    print('Pseudonymization map saved to pseud_map.csv')
