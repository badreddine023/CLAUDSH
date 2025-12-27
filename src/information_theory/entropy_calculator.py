import numpy as np
from collections import Counter

def calculate_shannon_entropy(data):
    """
    Calculate Shannon entropy of a sequence.
    """
    if not data:
        return 0
    
    counts = Counter(data)
    total = len(data)
    probabilities = [count / total for count in counts.values()]
    
    return -sum(p * np.log2(p) for p in probabilities if p > 0)

def calculate_conditional_entropy(x, y):
    """
    Calculate H(Y|X) - conditional entropy.
    """
    # Implementation placeholder
    pass

def calculate_kl_divergence(p, q):
    """
    Calculate Kullback-Leibler divergence between two distributions.
    """
    p = np.array(p)
    q = np.array(q)
    return np.sum(np.where(p != 0, p * np.log2(p / q), 0))

def calculate_redundancy(entropy, max_entropy):
    """
    Calculate redundancy ratio.
    """
    if max_entropy == 0:
        return 0
    return 1 - (entropy / max_entropy)
