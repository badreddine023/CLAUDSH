import re
import pandas as pd

def normalize_arabic(text):
    """
    Normalize Arabic text by removing diacritics and standardizing characters.
    """
    # Remove diacritics (tashkeel)
    text = re.sub(r'[\u064B-\u0652]', '', text)
    
    # Standardize Hamza
    text = re.sub(r'[إأآ]', 'ا', text)
    text = re.sub(r'ؤ', 'و', text)
    text = re.sub(r'ئ', 'ي', text)
    
    # Standardize Ta Marbuta
    text = re.sub(r'ة', 'ه', text)
    
    return text

def preprocess_quran_data(raw_data):
    """
    Preprocess raw Quran data into a structured DataFrame.
    """
    # Implementation placeholder for loading and tagging
    # 1. Load Quran text with metadata
    # 2. Normalize Arabic text
    # 3. Extract morphological roots (placeholder)
    # 4. Tag POS and roles (placeholder)
    
    processed_data = []
    for surah in raw_data.get('surahs', []):
        for verse in surah.get('verses', []):
            normalized_text = normalize_arabic(verse.get('arabic', ''))
            words = normalized_text.split()
            for word in words:
                processed_data.append({
                    'surah': surah.get('number'),
                    'ayah': verse.get('number'),
                    'word': word,
                    'root': None, # To be extracted
                    'pos': None,  # To be tagged
                    'role': None, # To be tagged
                    'theme': None, # To be tagged
                    'revelation_order': surah.get('revelation_order')
                })
    
    return pd.DataFrame(processed_data)
