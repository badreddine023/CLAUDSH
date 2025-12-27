"""
Quran Data Module
Manages the complete Quranic corpus with bilingual support.
"""

import json
import os
from typing import Dict, List, Optional, Tuple
from pathlib import Path


class QuranData:
    """
    Manages Quranic text data with bilingual support (Arabic and English).
    """

    def __init__(self, data_path: Optional[str] = None):
        """
        Initialize QuranData with path to quran.json file.
        
        Args:
            data_path: Path to quran.json file. If None, uses default location.
        """
        if data_path is None:
            # Default path relative to this file
            current_dir = Path(__file__).parent.parent
            data_path = current_dir / "data" / "quran.json"
        
        self.data_path = Path(data_path)
        self.quran_data = self._load_quran()
        self._build_indices()

    def _load_quran(self) -> Dict:
        """Load Quran data from JSON file."""
        try:
            with open(self.data_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Quran data file not found at {self.data_path}")
        except json.JSONDecodeError:
            raise ValueError(f"Invalid JSON in {self.data_path}")

    def _build_indices(self) -> None:
        """Build indices for efficient lookups."""
        self.word_index = {}  # word -> list of (surah, verse, word_data)
        self.root_index = {}  # root -> list of words
        
        for surah in self.quran_data.get('surahs', []):
            surah_num = surah['number']
            for verse in surah.get('verseList', []):
                verse_num = verse['number']
                for word_data in verse.get('words', []):
                    word = word_data.get('arabicWord', '')
                    root = word_data.get('root', '')
                    
                    if word:
                        if word not in self.word_index:
                            self.word_index[word] = []
                        self.word_index[word].append({
                            'surah': surah_num,
                            'verse': verse_num,
                            'data': word_data
                        })
                    
                    if root:
                        if root not in self.root_index:
                            self.root_index[root] = []
                        self.root_index[root].append(word)

    def get_surah(self, surah_number: int) -> Optional[Dict]:
        """
        Get a specific surah by number.
        
        Args:
            surah_number: Surah number (1-114)
            
        Returns:
            Surah data or None if not found
        """
        for surah in self.quran_data.get('surahs', []):
            if surah['number'] == surah_number:
                return surah
        return None

    def get_verse(self, surah_number: int, verse_number: int) -> Optional[Dict]:
        """
        Get a specific verse by surah and verse numbers.
        
        Args:
            surah_number: Surah number (1-114)
            verse_number: Verse number within the surah
            
        Returns:
            Verse data or None if not found
        """
        surah = self.get_surah(surah_number)
        if surah:
            for verse in surah.get('verseList', []):
                if verse['number'] == verse_number:
                    return verse
        return None

    def get_all_words(self) -> List[str]:
        """
        Get all unique words in the Quran.
        
        Returns:
            List of unique Arabic words
        """
        return list(self.word_index.keys())

    def get_word_occurrences(self, word: str) -> List[Tuple[int, int]]:
        """
        Get all occurrences of a word in the Quran.
        
        Args:
            word: Arabic word to search for
            
        Returns:
            List of (surah_number, verse_number) tuples
        """
        occurrences = []
        if word in self.word_index:
            for occurrence in self.word_index[word]:
                occurrences.append((occurrence['surah'], occurrence['verse']))
        return occurrences

    def get_word_frequency(self, word: str) -> int:
        """
        Get frequency of a word in the Quran.
        
        Args:
            word: Arabic word
            
        Returns:
            Number of occurrences
        """
        return len(self.get_word_occurrences(word))

    def get_words_by_root(self, root: str) -> List[str]:
        """
        Get all words that share the same root.
        
        Args:
            root: Arabic root (3-4 letters)
            
        Returns:
            List of words with this root
        """
        if root in self.root_index:
            return list(set(self.root_index[root]))
        return []

    def search_word(self, word: str, partial: bool = False) -> List[Dict]:
        """
        Search for words in the Quran.
        
        Args:
            word: Word to search for
            partial: If True, search for partial matches
            
        Returns:
            List of matching word entries with their occurrences
        """
        results = []
        
        for w in self.word_index.keys():
            if partial:
                if word in w:
                    results.append({
                        'word': w,
                        'frequency': len(self.word_index[w]),
                        'occurrences': self.get_word_occurrences(w)
                    })
            else:
                if w == word:
                    results.append({
                        'word': w,
                        'frequency': len(self.word_index[w]),
                        'occurrences': self.get_word_occurrences(w)
                    })
        
        return results

    def get_verse_text(self, surah_number: int, verse_number: int) -> Optional[Dict]:
        """
        Get complete verse text with Arabic and English.
        
        Args:
            surah_number: Surah number
            verse_number: Verse number
            
        Returns:
            Dictionary with arabic, english, and transliteration
        """
        verse = self.get_verse(surah_number, verse_number)
        if verse:
            return {
                'arabic': verse.get('arabic', ''),
                'english': verse.get('englishTranslation', ''),
                'transliteration': verse.get('transliteration', ''),
                'words': verse.get('words', [])
            }
        return None

    def get_surah_verses(self, surah_number: int) -> List[Dict]:
        """
        Get all verses in a surah.
        
        Args:
            surah_number: Surah number
            
        Returns:
            List of verse data
        """
        surah = self.get_surah(surah_number)
        if surah:
            return surah.get('verseList', [])
        return []

    def get_statistics(self) -> Dict:
        """
        Get overall statistics about the Quran.
        
        Returns:
            Dictionary with statistics
        """
        total_words = len(self.word_index)
        total_unique_roots = len(self.root_index)
        total_verses = sum(len(s.get('verseList', [])) for s in self.quran_data.get('surahs', []))
        
        return {
            'total_surahs': len(self.quran_data.get('surahs', [])),
            'total_verses': total_verses,
            'unique_words': total_words,
            'unique_roots': total_unique_roots,
            'total_word_instances': sum(len(occurrences) for occurrences in self.word_index.values())
        }


# Global instance
_quran_instance = None


def get_quran() -> QuranData:
    """Get or create the global Quran data instance."""
    global _quran_instance
    if _quran_instance is None:
        _quran_instance = QuranData()
    return _quran_instance


if __name__ == "__main__":
    # Example usage
    quran = get_quran()
    
    print("Quran Statistics:")
    stats = quran.get_statistics()
    for key, value in stats.items():
        print(f"  {key}: {value}")
    
    # Example: Get first surah
    surah_1 = quran.get_surah(1)
    print(f"\nSurah 1: {surah_1['name']} ({surah_1['nameArabic']})")
    
    # Example: Get first verse
    verse = quran.get_verse(1, 1)
    if verse:
        print(f"Verse 1:1 (Arabic): {verse['arabic']}")
        print(f"Verse 1:1 (English): {verse['englishTranslation']}")
