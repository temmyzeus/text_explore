"""Test's for the Readability module."""

from pathlib import Path

import pytest

from text_explore.readability import flesch_reading_ease, flesch_kincaid_grade

files_dir = Path("files/")


@pytest.fixture(scope="module")
def load_texts(files_dir: str = files_dir):
    all_text = dict()

    for file in files_dir.glob("*.txt"):
        with open(file, mode="r") as f:
            all_text[file.stem] = f.read()

    return all_text


def test_flesch_reading_ease(load_texts):
    error_rate = 3  # score should be +- error_rate
    for name, text in load_texts.items():
        score = flesch_reading_ease(text)
        print(name, score)


def test_flesch_kincaid_grade(load_texts):
    error_rate = 3  # score should be +- error_rate
    for name, text in load_texts.items():
        score = flesch_kincaid_grade(text)
        print(name, score)
