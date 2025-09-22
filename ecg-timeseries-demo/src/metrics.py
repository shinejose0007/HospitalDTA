
import numpy as np

def compute_basic_metrics(sig):
    return {'min': float(sig.min()), 'max': float(sig.max()), 'mean': float(sig.mean())}
