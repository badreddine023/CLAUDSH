"""
Linguistic Analysis Module
Performs Arabic linguistic processing and morphological analysis.
"""

import re
from typing import Dict, List, Set, Tuple, Optional
from collections import defaultdict
import json


class ArabicNormalizer:
    """Normalize Arabic text for analysis."""
    
    # Arabic diacritical marks (tashkeel)
    DIACRITICS = {
        '\u064B': '',  # FATHATAN
        '\u064C': '',  # DAMMATAN
        '\u064D': '',  # KASRATAN
        '\u064E': '',  # FATHA
        '\u064F': '',  # DAMMA
        '\u0650': '',  # KASRA
        '\u0651': '',  # SHADDA
        '\u0652': '',  # SUKUN
        '\u0653': '',  # MADDAH
        '\u0654': '',  # HAMZA ABOVE
        '\u0655': '',  # HAMZA BELOW
        '\u0656': '',  # SUBSCRIPT ALEF
        '\u0657': '',  # INVERTED DAMMA
        '\u0658': '',  # MARK NOON GHUNNA
        '\u0670': '',  # SUPERSCRIPT ALEF
    }
    
    # Character normalization
    CHAR_NORM = {
        '\u0649': '\u064A',  # ALEF MAKSURA -> YEH
        '\u0629': '\u0647',  # TEH MARBUTA -> HEH
    }

    @staticmethod
    def remove_diacritics(text: str) -> str:
        """Remove Arabic diacritical marks."""
        for diacritic, replacement in ArabicNormalizer.DIACRITICS.items():
            text = text.replace(diacritic, replacement)
        return text

    @staticmethod
    def normalize_characters(text: str) -> str:
        """Normalize Arabic character variations."""
        for char, replacement in ArabicNormalizer.CHAR_NORM.items():
            text = text.replace(char, replacement)
        return text

    @staticmethod
    def normalize(text: str) -> str:
        """Full normalization: remove diacritics and normalize characters."""
        text = ArabicNormalizer.remove_diacritics(text)
        text = ArabicNormalizer.normalize_characters(text)
        return text


class RootExtractor:
    """Extract Arabic roots from word forms."""
    
    # Common Arabic patterns and their root forms
    PATTERNS = {
        # Trilateral roots (most common)
        r'^ال(.{3})$': 1,  # Definite article prefix
        r'^و(.{3})$': 1,   # Conjunction prefix
        r'^ب(.{3})$': 1,   # Preposition prefix
        r'^ل(.{3})$': 1,   # Preposition prefix
        r'^ك(.{3})$': 1,   # Preposition prefix
    }

    @staticmethod
    def extract_root(word: str) -> str:
        """
        Extract the root from an Arabic word.
        
        Args:
            word: Arabic word (normalized)
            
        Returns:
            Root (3-4 letters)
        """
        word = ArabicNormalizer.normalize(word)
        
        # Remove common prefixes and suffixes
        # Prefixes: ال (the), و (and), ب (by), ل (for), ك (like)
        prefixes = ['ال', 'و', 'ب', 'ل', 'ك']
        for prefix in prefixes:
            if word.startswith(prefix):
                word = word[len(prefix):]
        
        # Suffixes: ه (his), ها (her), هم (their), ن (plural), ين (plural), ات (feminine plural)
        suffixes = ['ه', 'ها', 'هم', 'ن', 'ين', 'ات', 'ة', 'ي', 'ك', 'كم', 'كن']
        for suffix in suffixes:
            if word.endswith(suffix) and len(word) > 3:
                word = word[:-len(suffix)]
        
        # Return the root (typically 3-4 letters)
        return word[:4] if len(word) >= 3 else word

    @staticmethod
    def get_root_family(root: str) -> List[str]:
        """
        Get common word forms from a root.
        This is a simplified version - full implementation would use morphological tables.
        
        Args:
            root: Arabic root
            
        Returns:
            List of common word forms
        """
        # Simplified - in production, use morphological database
        forms = [root]
        
        # Add common patterns
        if len(root) >= 3:
            # Definite form
            forms.append('ال' + root)
            # With conjunction
            forms.append('و' + root)
            # With prepositions
            forms.append('ب' + root)
            forms.append('ل' + root)
        
        return forms


class LinguisticAnalyzer:
    """Comprehensive linguistic analysis of Quranic text."""
    
    def __init__(self):
        """Initialize the linguistic analyzer."""
        self.normalizer = ArabicNormalizer()
        self.root_extractor = RootExtractor()
        self.semantic_field_cache = {}

    def analyze_word(self, word: str) -> Dict:
        """
        Perform comprehensive analysis of a word.
        
        Args:
            word: Arabic word
            
        Returns:
            Dictionary with linguistic analysis
        """
        normalized = self.normalizer.normalize(word)
        root = self.root_extractor.extract_root(word)
        
        return {
            'original': word,
            'normalized': normalized,
            'root': root,
            'length': len(word),
            'letter_count': len(normalized),
            'is_definite': word.startswith('ال'),
            'root_family': self.root_extractor.get_root_family(root)
        }

    def extract_roots_from_text(self, text: str) -> List[str]:
        """
        Extract all roots from a text.
        
        Args:
            text: Arabic text
            
        Returns:
            List of unique roots
        """
        words = text.split()
        roots = set()
        
        for word in words:
            root = self.root_extractor.extract_root(word)
            if len(root) >= 3:
                roots.add(root)
        
        return sorted(list(roots))

    def calculate_morphological_similarity(self, word1: str, word2: str) -> float:
        """
        Calculate similarity between two words based on morphology.
        
        Args:
            word1: First Arabic word
            word2: Second Arabic word
            
        Returns:
            Similarity score (0-1)
        """
        root1 = self.root_extractor.extract_root(word1)
        root2 = self.root_extractor.extract_root(word2)
        
        # Same root = high similarity
        if root1 == root2:
            return 0.9
        
        # Check if roots share common letters
        common_letters = len(set(root1) & set(root2))
        max_letters = max(len(root1), len(root2))
        
        return common_letters / max_letters if max_letters > 0 else 0.0

    def build_semantic_field(self, word: str, all_words: List[str], threshold: float = 0.7) -> Dict:
        """
        Build semantic field for a word (related words).
        
        Args:
            word: Target word
            all_words: List of all words to search
            threshold: Similarity threshold for inclusion
            
        Returns:
            Dictionary with related words and similarity scores
        """
        cache_key = f"{word}_{threshold}"
        if cache_key in self.semantic_field_cache:
            return self.semantic_field_cache[cache_key]
        
        related_words = {}
        
        for candidate in all_words:
            if candidate == word:
                continue
            
            similarity = self.calculate_morphological_similarity(word, candidate)
            
            if similarity >= threshold:
                related_words[candidate] = similarity
        
        # Sort by similarity
        sorted_words = dict(sorted(related_words.items(), key=lambda x: x[1], reverse=True))
        
        result = {
            'word': word,
            'related_words': sorted_words,
            'count': len(sorted_words)
        }
        
        self.semantic_field_cache[cache_key] = result
        return result

    def get_word_forms(self, root: str) -> Dict:
        """
        Get information about word forms from a root.
        
        Args:
            root: Arabic root
            
        Returns:
            Dictionary with word form information
        """
        return {
            'root': root,
            'common_forms': self.root_extractor.get_root_family(root),
            'pattern_type': 'trilateral' if len(root) == 3 else 'quadrilateral'
        }

    def analyze_text_morphology(self, text: str) -> Dict:
        """
        Analyze morphological composition of text.
        
        Args:
            text: Arabic text
            
        Returns:
            Dictionary with morphological statistics
        """
        words = text.split()
        roots = self.extract_roots_from_text(text)
        
        definite_count = sum(1 for w in words if w.startswith('ال'))
        
        return {
            'total_words': len(words),
            'unique_words': len(set(words)),
            'unique_roots': len(roots),
            'definite_words': definite_count,
            'indefinite_words': len(words) - definite_count,
            'roots': roots
        }

    def find_cognates(self, word: str, all_words: List[str]) -> List[Tuple[str, float]]:
        """
        Find cognate words (words with same root).
        
        Args:
            word: Target word
            all_words: List of all words to search
            
        Returns:
            List of (word, similarity) tuples
        """
        root = self.root_extractor.extract_root(word)
        cognates = []
        
        for candidate in all_words:
            candidate_root = self.root_extractor.extract_root(candidate)
            if candidate_root == root and candidate != word:
                similarity = self.calculate_morphological_similarity(word, candidate)
                cognates.append((candidate, similarity))
        
        return sorted(cognates, key=lambda x: x[1], reverse=True)


# Global instance
_analyzer_instance = None


def get_analyzer() -> LinguisticAnalyzer:
    """Get or create the global linguistic analyzer instance."""
    global _analyzer_instance
    if _analyzer_instance is None:
        _analyzer_instance = LinguisticAnalyzer()
    return _analyzer_instance


if __name__ == "__main__":
    # Example usage
    analyzer = get_analyzer()
    
    # Example: Analyze a word
    word = "الحمد"
    analysis = analyzer.analyze_word(word)
    print(f"Analysis of '{word}':")
    for key, value in analysis.items():
        print(f"  {key}: {value}")
    
    # Example: Extract roots from text
    text = "الحمد لله رب العالمين"
    roots = analyzer.extract_roots_from_text(text)
    print(f"\nRoots in '{text}':")
    print(f"  {roots}")
    
    # Example: Morphological analysis of text
    morph = analyzer.analyze_text_morphology(text)
    print(f"\nMorphological Analysis:")
    for key, value in morph.items():
        print(f"  {key}: {value}")
