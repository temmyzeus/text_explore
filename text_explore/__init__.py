from .counts import (
    count_words,
    count_chars,
    count_stopwords,
    count_syllables,
    count_sentences,
)
from .readability import flesch_reading_ease, flesch_kincaid_grade

__version__ = "0.0.1"

all = ["counts", "readability"]


class TextExplore:
    def __init__(self, text: str) -> None:
        self.text = text

    def count_words(self):
        return count_words(self.text)

    def count_chars(self):
        return count_chars(self.text)

    def count_stopwords(self):
        return count_stopwords(self.text)

    def count_syllables(self):
        return count_syllables(self.text)

    def count_sentences(self):
        return count_sentences(self.text)

    def flesch_reading_ease(self):
        return flesch_reading_ease(self.text)

    def flesch_kincaid_grade(self):
        return flesch_kincaid_grade(self.text)
