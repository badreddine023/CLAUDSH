import numpy as np
import pandas as pd
from collections import defaultdict

class MarkovAnalyzer:
    def __init__(self, order=1):
        self.order = order
        self.transitions = defaultdict(lambda: defaultdict(int))
        self.states = set()

    def fit(self, sequence):
        """
        Build transition counts from a sequence.
        """
        for i in range(len(sequence) - self.order):
            state = tuple(sequence[i:i+self.order])
            next_item = sequence[i+self.order]
            self.transitions[state][next_item] += 1
            self.states.add(state)

    def get_transition_matrix(self):
        """
        Convert transition counts to probabilities.
        """
        matrix = {}
        for state, next_states in self.transitions.items():
            total = sum(next_states.values())
            matrix[state] = {k: v/total for k, v in next_states.items()}
        return matrix

    def calculate_stationary_distribution(self):
        """
        Placeholder for stationary distribution calculation.
        """
        pass

    def identify_absorbing_states(self):
        """
        Identify states that only transition to themselves.
        """
        absorbing = []
        matrix = self.get_transition_matrix()
        for state, transitions in matrix.items():
            if len(transitions) == 1 and state in transitions:
                absorbing.append(state)
        return absorbing
