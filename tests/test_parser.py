import pytest

from ..src.parser import (
    create_feed_row,
    get_row_string_from_raw_input,
    get_words_from_string,
    parse_raw_input,
)

input1 = ""
input2 = """3 boxes of chocolates at 12.99
1 book at 10.00
1 bottle of parfume at 39.99"""
input3 = """3 boxes of chocolates at 12.99

1 book at 10.00


1 bottle of parfume at 39.99"""

s_input1 = "3 apples in the basket, 2.99"
s_input2 = "book"
s_input3 = "1 book at 7.99"

l_input1 = ["1", "book", "at", "7.99"]
l_input2 = ["3", "box", "of", "imported", "chocolates", "at", "12.70"]


def test_row_parser():
    # passing an empty string should raise ValueError
    with pytest.raises(ValueError):
        get_row_string_from_raw_input(input1)
    # passing an input that is not a string should raise a TypeError
    with pytest.raises(TypeError):
        get_row_string_from_raw_input(2)
    with pytest.raises(TypeError):
        get_row_string_from_raw_input(["one", "two"])
    # passing an input with 3 rows should produce a tuble with 3 elements
    assert len(get_row_string_from_raw_input(input2)) == 3
    assert type(get_row_string_from_raw_input(input2)) is tuple
    # empty lines in input should be ignored
    assert len(get_row_string_from_raw_input(input3)) == 3
    assert type(get_row_string_from_raw_input(input3)) is tuple


def test_string_parser():
    # passing a string without "at" separator should raise ValueError
    with pytest.raises(ValueError):
        get_words_from_string(s_input1)
    # passing a string formatted wrong should raise ValueError
    with pytest.raises(ValueError):
        get_words_from_string(s_input2)
    # passing any type of input that is not a string should raise TypeError
    with pytest.raises(TypeError):
        get_words_from_string(12)
    # passing a valid input should generate a list with one element
    # for each word separated by a space
    assert len(get_words_from_string(s_input3)) == 4
    assert type(get_words_from_string(s_input3)) is list
