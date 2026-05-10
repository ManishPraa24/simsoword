# Use this code, if python cannot find the module 'simsoword'

# import sys
# import os

# sys.path.append(
#     os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# )

from simsoword.preprocess import normalize_text


def test_lowercase():
    assert normalize_text("HELLO") == "hello"


def test_remove_special_characters():
    assert normalize_text("night123!!") == "night"


def test_space_error():
    try:
        normalize_text("new york")
    except ValueError:
        assert True
