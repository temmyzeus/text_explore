"""Text explore `readability` module"""

from typing import Union

from text_explore.counts import count_syllables

def flesch_reading_ease(text: str, tokenizer = None) -> float:
    """Get's the Flesch Reading Ease test score for text.

    The Flesch-Kincaid Readability Tests are readability tests designed to \
    indicate how difficult a passage in English is to understand.\
    It was developed Rudolf Flesch in the year 1948.

    Parameters:
    ----------
    text: str
        Text to run test on.
    tokenizer: default = None
        Object with a tokenizer method to tokenize the text.

    Returns:
    -------
        flesch_score: float
    """
    assert isinstance(text, str), f'Text must be a  string, not a {type(text)}'

    if tokenizer:
        word_tokens = tokenizer.tokenize(text)
        total_words: int = len(word_tokens)
    else:
        word_tokens = text.split()
        total_words: int = len(word_tokens)
    
    total_sentences: int = len(text.split('\n')) # split text by newlines to get number of sentences.

    total_syllables: int = sum([count_syllables(word) for word in word_tokens])

    score = 206.835 - (1.015 * (total_words / total_sentences)) - (84.6 * (total_syllables / total_words))
    return round(score, 1)

def flesch_kincaid_grade(text:str, tokenizer = None) -> float:
    """Get's the Flesch-Kincaid Grade Level test score for text.

    The Flesch-Kincaid Readability Tests are readability tests designed to \
    indicate how difficult a passage in English is to understand.\
    It was developed Rudolf Flesch in the year 1948.

    Parameters:
    ----------
    text: str
        Text to run test on
    tokenizer: default = None
        Object with a tokenizer method to tokenize the text.

    Returns:
    --------
        flesch-kincaid grade level score: float
    """
    assert isinstance(text, str), f'Text must be a  string, not a {type(text)}'

    if tokenizer:
        word_tokens = tokenizer.tokenize(text)
        total_words: int = len(word_tokens)
    else:
        word_tokens = text.split()
        total_words: int = len(word_tokens)
    
    total_sentences: int = len(text.split('\n')) # split text by newlines to get number of sentences.

    total_syllables: int = sum([count_syllables(word) for word in word_tokens])

    score = (0.39 * (total_words / total_sentences)) + (11.8 * (total_syllables / total_words)) - 15.59
    return round(score, 1)

class FleschKincaidTest:
    """Get's the Flesch Kincaid readability test score for text.

    The Flesch-Kincaid readability tests are readability tests designed to \
    indicate how difficult a passage in English is to understand.\
    It was developed Rudolf Flesch in the year 1948.

    Arguments:
    ----------
        text: str

    Returns:
    -------
        flesch_score: float
    """
    pass
