"""
Mathematical Analysis Module
Statistical and mathematical analysis of Quranic text.
"""

import json
from typing import Dict, List, Tuple, Optional
from collections import Counter, defaultdict
import math


class WordFrequencyAnalyzer:
    """Analyze word frequencies in the Quran."""
    
    def __init__(self, quran_data: Dict):
        """
        Initialize with Quran data.
        
        Args:
            quran_data: Dictionary containing Quran structure
        """
        self.quran_data = quran_data
        self.word_frequencies = {}
        self.root_frequencies = {}
        self._calculate_frequencies()
    
    def _calculate_frequencies(self) -> None:
        """Calculate word and root frequencies."""
        word_counter = Counter()
        root_counter = Counter()
        
        for surah in self.quran_data.get('surahs', []):
            for verse in surah.get('verseList', []):
                for word_data in verse.get('words', []):
                    word = word_data.get('arabicWord', '')
                    root = word_data.get('root', '')
                    
                    if word:
                        word_counter[word] += 1
                    if root:
                        root_counter[root] += 1
        
        self.word_frequencies = dict(word_counter)
        self.root_frequencies = dict(root_counter)
    
    def get_word_frequency(self, word: str) -> int:
        """Get frequency of a specific word."""
        return self.word_frequencies.get(word, 0)
    
    def get_root_frequency(self, root: str) -> int:
        """Get frequency of a specific root."""
        return self.root_frequencies.get(root, 0)
    
    def get_top_words(self, n: int = 20) -> List[Tuple[str, int]]:
        """Get top N most frequent words."""
        return sorted(self.word_frequencies.items(), key=lambda x: x[1], reverse=True)[:n]
    
    def get_top_roots(self, n: int = 20) -> List[Tuple[str, int]]:
        """Get top N most frequent roots."""
        return sorted(self.root_frequencies.items(), key=lambda x: x[1], reverse=True)[:n]
    
    def get_frequency_distribution(self) -> Dict:
        """Get distribution statistics of word frequencies."""
        frequencies = list(self.word_frequencies.values())
        
        if not frequencies:
            return {}
        
        total = sum(frequencies)
        avg = total / len(frequencies)
        
        # Calculate standard deviation
        variance = sum((x - avg) ** 2 for x in frequencies) / len(frequencies)
        std_dev = math.sqrt(variance)
        
        return {
            'total_unique_words': len(self.word_frequencies),
            'total_word_instances': total,
            'average_frequency': avg,
            'std_deviation': std_dev,
            'min_frequency': min(frequencies),
            'max_frequency': max(frequencies),
            'median_frequency': sorted(frequencies)[len(frequencies) // 2]
        }
    
    def get_frequency_by_surah(self, word: str) -> Dict[int, int]:
        """Get frequency of a word in each surah."""
        frequencies = defaultdict(int)
        
        for surah in self.quran_data.get('surahs', []):
            surah_num = surah['number']
            for verse in surah.get('verseList', []):
                for word_data in verse.get('words', []):
                    if word_data.get('arabicWord', '') == word:
                        frequencies[surah_num] += 1
        
        return dict(frequencies)


class SimilarityCalculator:
    """Calculate similarity between words."""
    
    @staticmethod
    def levenshtein_distance(s1: str, s2: str) -> int:
        """Calculate Levenshtein distance between two strings."""
        if len(s1) < len(s2):
            return SimilarityCalculator.levenshtein_distance(s2, s1)
        
        if len(s2) == 0:
            return len(s1)
        
        previous_row = range(len(s2) + 1)
        for i, c1 in enumerate(s1):
            current_row = [i + 1]
            for j, c2 in enumerate(s2):
                insertions = previous_row[j + 1] + 1
                deletions = current_row[j] + 1
                substitutions = previous_row[j] + (c1 != c2)
                current_row.append(min(insertions, deletions, substitutions))
            previous_row = current_row
        
        return previous_row[-1]
    
    @staticmethod
    def levenshtein_similarity(s1: str, s2: str) -> float:
        """Calculate normalized Levenshtein similarity (0-1)."""
        distance = SimilarityCalculator.levenshtein_distance(s1, s2)
        max_len = max(len(s1), len(s2))
        
        if max_len == 0:
            return 1.0
        
        return 1.0 - (distance / max_len)
    
    @staticmethod
    def jaccard_similarity(s1: str, s2: str) -> float:
        """Calculate Jaccard similarity based on character sets."""
        set1 = set(s1)
        set2 = set(s2)
        
        if len(set1 | set2) == 0:
            return 1.0
        
        intersection = len(set1 & set2)
        union = len(set1 | set2)
        
        return intersection / union
    
    @staticmethod
    def cosine_similarity(word1: str, word2: str) -> float:
        """Calculate cosine similarity based on character frequency."""
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        # Calculate dot product
        dot_product = sum(counter1[char] * counter2[char] for char in counter1 if char in counter2)
        
        # Calculate magnitudes
        magnitude1 = math.sqrt(sum(count ** 2 for count in counter1.values()))
        magnitude2 = math.sqrt(sum(count ** 2 for count in counter2.values()))
        
        if magnitude1 == 0 or magnitude2 == 0:
            return 0.0
        
        return dot_product / (magnitude1 * magnitude2)
    
    @staticmethod
    def combined_similarity(word1: str, word2: str, weights: Optional[Dict] = None) -> float:
        """Calculate combined similarity using multiple metrics."""
        if weights is None:
            weights = {
                'levenshtein': 0.4,
                'jaccard': 0.3,
                'cosine': 0.3
            }
        
        lev = SimilarityCalculator.levenshtein_similarity(word1, word2)
        jac = SimilarityCalculator.jaccard_similarity(word1, word2)
        cos = SimilarityCalculator.cosine_similarity(word1, word2)
        
        return (
            lev * weights['levenshtein'] +
            jac * weights['jaccard'] +
            cos * weights['cosine']
        )


class PatternDetector:
    """Detect mathematical patterns in Quranic text."""
    
    def __init__(self, quran_data: Dict):
        """Initialize with Quran data."""
        self.quran_data = quran_data
    
    def get_verse_statistics(self, surah_num: int, verse_num: int) -> Dict:
        """Get statistics for a specific verse."""
        for surah in self.quran_data.get('surahs', []):
            if surah['number'] == surah_num:
                for verse in surah.get('verseList', []):
                    if verse['number'] == verse_num:
                        words = verse.get('words', [])
                        arabic_text = verse.get('arabic', '')
                        
                        return {
                            'word_count': len(words),
                            'letter_count': len(arabic_text.replace(' ', '')),
                            'unique_words': len(set(w.get('arabicWord', '') for w in words)),
                            'unique_roots': len(set(w.get('root', '') for w in words)),
                            'arabic_text': arabic_text,
                            'english_translation': verse.get('englishTranslation', '')
                        }
        
        return {}
    
    def get_surah_statistics(self, surah_num: int) -> Dict:
        """Get statistics for a complete surah."""
        for surah in self.quran_data.get('surahs', []):
            if surah['number'] == surah_num:
                verses = surah.get('verseList', [])
                all_words = []
                all_roots = set()
                total_letters = 0
                
                for verse in verses:
                    words = verse.get('words', [])
                    all_words.extend([w.get('arabicWord', '') for w in words])
                    all_roots.update(w.get('root', '') for w in words)
                    total_letters += len(verse.get('arabic', '').replace(' ', ''))
                
                return {
                    'surah_number': surah_num,
                    'surah_name': surah.get('name', ''),
                    'verse_count': len(verses),
                    'total_words': len(all_words),
                    'unique_words': len(set(all_words)),
                    'unique_roots': len(all_roots),
                    'total_letters': total_letters,
                    'average_words_per_verse': len(all_words) / len(verses) if verses else 0,
                    'average_letters_per_verse': total_letters / len(verses) if verses else 0
                }
        
        return {}
    
    def find_repeated_patterns(self, min_frequency: int = 3) -> Dict:
        """Find words that appear frequently."""
        word_freq = Counter()
        
        for surah in self.quran_data.get('surahs', []):
            for verse in surah.get('verseList', []):
                for word_data in verse.get('words', []):
                    word = word_data.get('arabicWord', '')
                    if word:
                        word_freq[word] += 1
        
        patterns = {word: freq for word, freq in word_freq.items() if freq >= min_frequency}
        return dict(sorted(patterns.items(), key=lambda x: x[1], reverse=True))


def analyze_quran_file(file_path: str) -> Dict:
    """
    Analyze a Quran JSON file and return comprehensive statistics.
    
    Args:
        file_path: Path to quran.json file
        
    Returns:
        Dictionary with analysis results
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        quran_data = json.load(f)
    
    # Initialize analyzers
    freq_analyzer = WordFrequencyAnalyzer(quran_data)
    pattern_detector = PatternDetector(quran_data)
    
    # Get results
    results = {
        'frequency_distribution': freq_analyzer.get_frequency_distribution(),
        'top_20_words': freq_analyzer.get_top_words(20),
        'top_20_roots': freq_analyzer.get_top_roots(20),
        'surah_statistics': [
            pattern_detector.get_surah_statistics(surah['number'])
            for surah in quran_data.get('surahs', [])
        ]
    }
    
    return results


if __name__ == "__main__":
    import sys
    from pathlib import Path
    
    # Find quran.json
    current_dir = Path(__file__).parent.parent
    quran_file = current_dir / "data" / "quran.json"
    
    if not quran_file.exists():
        print(f"Error: {quran_file} not found")
        sys.exit(1)
    
    print("=" * 60)
    print("QURANIC WORD FREQUENCY ANALYSIS")
    print("=" * 60)
    
    with open(quran_file, 'r', encoding='utf-8') as f:
        quran_data = json.load(f)
    
    # Analyze frequencies
    analyzer = WordFrequencyAnalyzer(quran_data)
    
    print("\n📊 FREQUENCY DISTRIBUTION STATISTICS:")
    print("-" * 60)
    stats = analyzer.get_frequency_distribution()
    for key, value in stats.items():
        print(f"  {key}: {value:.2f}" if isinstance(value, float) else f"  {key}: {value}")
    
    print("\n🔝 TOP 20 MOST FREQUENT WORDS:")
    print("-" * 60)
    for i, (word, freq) in enumerate(analyzer.get_top_words(20), 1):
        print(f"  {i:2d}. {word:15s} → {freq:4d} occurrences")
    
    print("\n🔝 TOP 20 MOST FREQUENT ROOTS:")
    print("-" * 60)
    for i, (root, freq) in enumerate(analyzer.get_top_roots(20), 1):
        print(f"  {i:2d}. {root:10s} → {freq:4d} occurrences")
    
    # Test similarity
    print("\n🔗 WORD SIMILARITY EXAMPLES:")
    print("-" * 60)
    test_pairs = [
        ("الحمد", "الشكر"),
        ("الله", "اله"),
        ("رب", "ربب"),
    ]
    
    for word1, word2 in test_pairs:
        sim = SimilarityCalculator.combined_similarity(word1, word2)
        print(f"  '{word1}' ↔ '{word2}': {sim:.3f}")
    
    # Surah statistics
    print("\n📈 SURAH STATISTICS (First 3 Surahs):")
    print("-" * 60)
    detector = PatternDetector(quran_data)
    for surah_num in range(1, 4):
        stats = detector.get_surah_statistics(surah_num)
        print(f"\n  Surah {stats.get('surah_number')}: {stats.get('surah_name')}")
        print(f"    Verses: {stats.get('verse_count')}")
        print(f"    Total words: {stats.get('total_words')}")
        print(f"    Unique words: {stats.get('unique_words')}")
        print(f"    Unique roots: {stats.get('unique_roots')}")
        print(f"    Total letters: {stats.get('total_letters')}")
    
    print("\n" + "=" * 60)
    print("Analysis complete!")
