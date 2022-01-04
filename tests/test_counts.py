import pytest
from nltk.corpus import stopwords
from nltk.tokenize import WordPunctTokenizer

from text_explore import (
                        count_words, 
                        count_chars, 
                        count_stopwords, 
                        count_syllables_1, 
                        count_syllables_2
                        )


def test_count_words():
    sample_text_1 = 'It\'s a new day, get up and work.'

    sample_text_2 = 'Lorem ipsum dolor sit amet, et debet '\
                    'errem nec. Sed labores maiorum abhorreant '\
                    'ei. Vim mentitum explicari id, tota postulant '\
                    'ullamcorper eos ei. Reque iriure detracto quo ne, '\
                    'his dicat nulla salutandi ne. Est at malis nostrud '\
                    'intellegebat, posse epicurei mea ut.'

    sample_text_3 = r'''
            thanks undeletion was more than i'd hoped for i'm researching the \
            status of texas government including local government copyright \
            status but it's slow going apparently works of the florida government \
            are usually public domain but we don't have a similar article on \
            texas so i guess i'll have to research the old fashioned non lazy \
            actually reliable way or ask the copyright help desk like you \
            suggested in the meantime i'm using the fair use rationale since \
            it's valid while the image is used in an article thanks again.
            '''

    sample_text_4 = 211
    tokenizer = WordPunctTokenizer()
    assert count_words(sample_text_1) == 8
    assert count_words(sample_text_2) == 42
    assert count_words(sample_text_3, WordPunctTokenizer) == 111
    assert count_words(sample_text_3, tokenizer) == 111

    # assert TypeError is raised for invalid data type.
    with pytest.raises(TypeError):
        count_words(sample_text_4)

    # assert AttributeError is raised for object with no .tokenize() method
    with pytest.raises(AttributeError):
        count_words(sample_text_1, object)


def test_count_chars():
    sample_text_1 = 'Programmers love Hello World!!'
    sample_text_2 = ['Hello', 'World']
    assert count_chars(sample_text_1) == 27
    assert count_chars(sample_text_1, include_spaces=True) == 30

    with pytest.raises(TypeError):
        count_chars(sample_text_2)


def test_count_stopwords():
    sample_text_1 = r'''
                thanks undeletion was more than i'd hoped for i'm researching the \
                status of texas government including local government copyright \
                status but it's slow going apparently works of the florida government \
                are usually public domain but we don't have a similar article on \
                texas so i guess i'll have to research the old fashioned non lazy \
                actually reliable way or ask the copyright help desk like you \
                suggested in the meantime i'm using the fair use rationale since \
                it's valid while the image is used in an article thanks again.
                '''

    # test while using an iterable
    def stopwords_gen():
        stopwords_set = stopwords.words('english')
        for word in stopwords_set:
            yield word

    assert count_stopwords(sample_text_1) == 34

def test_count_syllables():
    sample_syllable_counts = {
        'epidemic': 4,
        'plagiarism': 3,
        'bootlegging': 3,
        21: 23,
        (1, 65, 34): 89,
        546.7: 67
    }

    for word, count in sample_syllable_counts.items():
        if not isinstance(word, str):
            with pytest.raises(TypeError):
                syl_count = count_syllables_2(word)
            continue # make sure this `continue` keyword isn't under the context manager above.

        syl_count = count_syllables_2(word)
        assert syl_count == count
