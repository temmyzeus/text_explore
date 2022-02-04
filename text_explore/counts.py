import re
from typing import Iterable

from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
from tqdm import tqdm


def count_words(text: str, tokenizer=None) -> int:
    """
    Count number of words in a text.

    Arguments:
    ---------
    text: str
        Text whose words are to be counted.
    tokenizer: default=None
        Object with a tokenize method. Either instantiated or not works. \
        If tokenizer is available, it is used to tokenize words before counted.

    Returns:
    -------
    Number of Words: int
        Length of words in text.
    """
    # should text input be a text, or should it accept it as long as it can be changed to text??
    if not isinstance(text, str):
        raise TypeError("Text must be in string format not {}".format(type(text)))

    if tokenizer:
        # assert hasattr(tokenizer, 'tokenize'), 'Tokenizer object must has a `tokenize` method!!'
        # if tokenize object doesn't have a  tokenize method
        if not hasattr(tokenizer, "tokenize"):
            raise AttributeError("Tokenizer object must has a `tokenize` method!!")

        # ensure it works if class is instantiated or not
        try:
            text_tokens = tokenizer().tokenize(text)
        except TypeError:
            text_tokens = tokenizer.tokenize(text)
        finally:
            return len(text_tokens)
    else:
        text_tokens = text.split()

    return len(text_tokens)


def count_chars(text: str, include_spaces=False) -> int:
    """
    Count number of characters in a text.

    Arguments:
    ---------
    text: str
        Text whose words are to be counted.
    include_spaces: bool, default=False
        Count spaces as characters.

    Returns:
    -------
    Number of Characters: int
        Length of words in text.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be in string format not {}".format(type(text)))

    if not include_spaces:
        text = text.replace(" ", "")  # replace space with no space

    return len(text)


def count_stopwords(
    text: str, language: str = "english", tokenizer=None, stopwords_set: Iterable = None
) -> int:
    """
    Count number of stopwords in a text.

    Arguments:
    ---------
    text: str
        Text whose words are to be counted.
    language: str, default='english'
        Language stopwords to use, this depends on the nltk available stopwords languages
    tokenizer: default=None
        Object with a tokenize method. Either instantiated or not works. \
        If tokenizer is available, it is used to tokenize words before counted.
    stopwords_set: Iterable, default=None
        An iterable (preferably a set) containing stopwords to use incase of using custom stopwords.

    Returns:
    -------
    Number of Stopwords: int
        Length of stopwords in text.
    """
    if not isinstance(text, str):
        raise TypeError("Text must be in string format not {}".format(type(text)))

    # nltk has an option of selecting the langauge, selecting english directly in code
    # will make it segregated only for english language
    if stopwords_set:
        stopwords_set = set(
            stopwords_set
        )  # convert iterable to set eliminating duplicates and making it faster
    else:
        stopwords_set = set(stopwords.words(language))

    if tokenizer:
        # if tokenize object doesn't have a  tokenize method
        if not hasattr(tokenizer, "tokenize"):
            raise AttributeError("Tokenizer object must has a `tokenize` method!!")

        # ensure it works if class is instantiated or not
        try:
            text_tokens = tokenizer().tokenize(text)
        except TypeError:
            text_tokens = tokenizer.tokenize(text)
        finally:
            return len(text_tokens)
    else:
        text_tokens = text.split()

    stopwords_count = len([word for word in tqdm(text_tokens) if word in stopwords_set])
    return stopwords_count


def count_syllables(word: str) -> int:
    """Count number of syllables in a word.

    Parameters:
    ----------
    word: str
        Word to count syllables in.

    Returns:
    --------
    syllables_count: int
        Number of syllables in word
    """
    if not isinstance(word, str):
        raise TypeError(f"Word should be a string, not a {type(word)}")

    word = word.lower()
    count = 0
    vowels = "aeiouy"
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    if word.endswith("e"):
        count -= 1
    if count == 0:
        count += 1
    return count


def count_sentences(text: str) -> int:
    """
    Count number of Sentences in a text.

    Arguments:
    ---------
    text: str
        Text to count sentences in.

    Returns:
    -------
    n_sentences: int
        Number of Sentences in text.
    """

    sentence_tokens: list = sent_tokenize(text)
    n_sentences = len(sentence_tokens)
    return n_sentences
