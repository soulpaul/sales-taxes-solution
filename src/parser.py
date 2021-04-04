from collections import namedtuple
from decimal import *

Feed_Row = namedtuple("Feed_Row", "qty product price")


def create_feed_row(word_list: list):
    if type(word_list) is not list:
        raise TypeError("Please provide a list as input")
    qty = int(word_list[0])
    price = Decimal(word_list[-1])
    # imported word should always lead product description
    if "imported" in word_list:
        word_list.pop(word_list.index("imported"))
        word_list.insert(1, "imported")
    # product name should go from position 1 to -2 of the list
    product = " ".join(word_list[1:-2])
    return Feed_Row(qty=qty, product=product, price=price)


def get_row_string_from_raw_input(input: str):
    if type(input) is not str:
        raise TypeError("Please provide a string as input")
    if len(input) > 0:
        return tuple(filter(filter_empty_strings, input.split("\n")))
    else:
        raise ValueError("No input provided")


def get_words_from_string(string: str):
    if type(string) is not str:
        raise TypeError("Please provide a string as input")
    words = string.split(" ")
    # to be valid a string should contain at least 4 words
    # quantity / product name / "at" / price
    # if has less then 4 words we can safely assume it's not valid
    # "at" is the separator between product name and price
    # should always be in the second-last position, if it's
    # not we can assume the row is not properly formatted
    if len(words) > 3 and words[-2].lower() == "at":
        return words
    else:
        raise ValueError(
            f'String "{string}" not properly formatted. Impossible to parse'
        )


def filter_empty_strings(string):
    if len(string) > 0:
        return True
    return False


def parse_raw_input(input: str):
    row_strings = get_row_string_from_raw_input(input)
    row_words = [get_words_from_string(row_string) for row_string in row_strings]
    feed_rows = tuple(map(create_feed_row, row_words))
    return feed_rows

