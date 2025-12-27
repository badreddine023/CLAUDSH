import os
import yaml
import json
from preprocessing.text_processor import preprocess_quran_data
from local_analysis.markov_chains import MarkovAnalyzer
from information_theory.entropy_calculator import calculate_shannon_entropy

class QuranHyperAnalysisPipeline:
    def __init__(self, config_path='config.yaml'):
        with open(config_path, 'r') as f:
            self.config = yaml.safe_load(f)
        
    def run(self):
        print("Starting Quran Hyper-Analysis Pipeline...")
        
        # 1. Load Data
        raw_data_path = os.path.join(self.config['paths']['data_raw'], 'quran_text.json')
        # For now, we'll check if the file exists, otherwise use the one in the root data folder
        if not os.path.exists(raw_data_path):
            raw_data_path = 'data/quran.json'
            
        with open(raw_data_path, 'r') as f:
            raw_data = json.load(f)
            
        # 2. Preprocessing
        print("Preprocessing text...")
        df = preprocess_quran_data(raw_data)
        
        # 3. Local Analysis (Markov)
        print("Running Markov analysis...")
        analyzer = MarkovAnalyzer(order=1)
        analyzer.fit(df['word'].tolist())
        markov_results = analyzer.get_transition_matrix()
        
        # 4. Information Theory
        print("Calculating entropy...")
        entropy = calculate_shannon_entropy(df['word'].tolist())
        
        # 5. Save Results
        output_dir = self.config['paths']['data_processed']
        os.makedirs(output_dir, exist_ok=True)
        
        # Placeholder for saving
        print(f"Analysis complete. Global Word Entropy: {entropy:.4f}")
        
if __name__ == "__main__":
    pipeline = QuranHyperAnalysisPipeline()
    pipeline.run()
