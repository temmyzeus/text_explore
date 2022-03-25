# Text_Explore

A Python Library to perform Exploratory Data Analysis on Text

Install Package

```bash
pip install text_explore
```

## Using Package

1. Access from class

    ```python
    # Access from a single class
    from text_explore import TextExplore


    text = """US actor Jussie Smollett has been sentenced to 150 days in jail after a jury found he lied to police about being the victim of a hate crime.

    The former Empire star, 39, was found guilty in December of five charges of felony disorderly conduct after making false reports about the hoax attack.

    The sentence also includes 30 months of probation and $145,000 (£110,000) in restitution and fines.

    Following the sentence, Smollett said: "I did not do this!"

    The trial stemmed from an incident three years ago when Smollett said he was attacked by two assailants.

    The actor, who is black and gay, said the attackers shouted slurs at him and a Trump slogan, dumped a "chemical substance" on him and tied a noose around his neck while he was walking late at night in January 2019."""

    words = ["lean", "thought", "mean", "flower", "yeast", "vehicle", "feel", "broadcast", "dreamed", "resources"]

    doc = TextExplore(text)

    # Count Number of Words in Text
    print("Word Count:", doc.count_words())

    # Count Number of Characters in Text
    print("Characters Count:", doc.count_chars())

    # Count Number of Stopwords in Text
    print("Stopwords Count", doc.count_stopwords())

    # Count Number of Syllables in Text
    print("Syllables Count:", doc.count_syllables())

    # Count Number of Sentences in Text
    print("Sentences Count:", doc.count_sentences())

    # Flesch reading ease score
    print("Flesch reading ease:", doc.flesch_reading_ease())

    # Flesch kincaid grade score
    print("Flesch kincaid grade:", doc.flesch_kincaid_grade())
    ```

2. Access individual functions

    ```python
    # Access individual functions
    from text_explore.counts import (
        count_words,
        count_chars,
        count_stopwords,
        count_syllables,
        count_sentences,
    )
    from text_explore.readability import (
        flesch_kincaid_grade, 
        flesch_reading_ease
    )


    # Count Number of Syllables in a Word
    for word in words:
        print(f"{word} syllables count:", count_syllables(word))

    # Count Number of Words in Text
    print("Word Count:", count_words(text))

    # Count Number of Characters in Text
    print("Characters Count:", count_chars(text))

    # Count Number of Stopwords in Text
    print("Stopwords Count", count_stopwords(text))

    # Count Number of Sentences in Text
    print("Sentences Count:", count_sentences(text))

    # Flesch reading ease score
    print("Flesch reading ease:", flesch_reading_ease(text))

    # Flesch kincaid grade score
    print("Flesch kincaid grade:", flesch_kincaid_grade(text))
    ```
