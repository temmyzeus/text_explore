# Use Typer or Argparse for Argument Parsing and simply return results on the file

import argparse
import os

from . import TextExplore
from .counts import count_syllables


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        "Text Explore CLI", description="Run Text Explore directly on .txt a file"
    )
    # To Do: Allow more than 1 path, multiple filenames as list
    parser.add_argument(
        "--filename",
    )
    args = parser.parse_args()

    # Add guard clauses to check if file/folder doesn't exist
    if not os.path.exists(args.filename):
        raise FileNotFoundError(f"No such file: {args.filename}")

    # Then check if it's a dir, doesn't allow folder yet
    if os.path.isdir(args.filename):
        raise IsADirectoryError(
            f"Directory is not allowed, {args.filename} is a directory"
        )

    ext = os.path.splitext(args.filename)[-1]
    if not (ext == ".txt"):
        # To Do: Check if Error Type is correct
        raise TypeError(f"File must be a .txt file, not a {ext} file")

    with open(args.filename, mode="r") as f:
        text = f.read()

    doc = TextExplore(text)
    print("Word Count:", doc.count_words())
    print("Characters Count:", doc.count_chars())
    print("Stopwords Count", doc.count_stopwords())
    # Reimplement this in terms of average syllables counts
    print(
        "Total Syllables Count:",
        sum([count_syllables(word) for word in text.split(" ")]),
    )
    print("Sentences Count:", doc.count_sentences())
    print("Flesch reading ease:", doc.flesch_reading_ease())
    print("Flesch kincaid grade:", doc.flesch_kincaid_grade())
