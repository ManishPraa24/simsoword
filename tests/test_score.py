# Use this code, if python cannot find the module 'simsoword'

# import sys
# import os

# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# )

from simsoword.metrics import (
    jaro_winkler_score,
    levenshtein_score
)


def test_jaro_score():
    score = jaro_winkler_score("nite", "night")

    assert isinstance(score, float)
    assert 0 <= score <= 100


def test_levenshtein_score():
    score = levenshtein_score("nite", "night")

    assert isinstance(score, float)
    assert 0 <= score <= 100


def test_empty_strings():
    score = levenshtein_score("", "")

    assert score == 100.0