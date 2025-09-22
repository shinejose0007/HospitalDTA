
import argparse
from wfdb import rdrecord
import numpy as np
import os

def load_sample():
    # Placeholder: user should download a small PhysioNet record and place in data/
    sample_path = os.path.join('data','sample_record')
    if not os.path.exists(sample_path + '.dat'):
        print('No local sample record found. Please download a small PhysioNet record to data/ and set --record accordingly.')
        return
    rec = rdrecord(sample_path)
    print('Loaded record:', rec.__dict__.keys())

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--record', default='sample', help='Record name or path')
    args = parser.parse_args()
    if args.record == 'sample':
        load_sample()
    else:
        print('Custom record flow not implemented in this demo.')
