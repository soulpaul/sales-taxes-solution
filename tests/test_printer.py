import pytest
from decimal import *

from ..src.printer import (
    is_exempt,
    is_imported,
    is_word_in_phrase,
    get_row_tax_percentage,
    tax_round_up,
)


def test_tax_rounding():
    assert tax_round_up(Decimal("2.01")) == Decimal("2.05")
    assert tax_round_up(Decimal("13.55")) == Decimal("13.55")
    assert tax_round_up(Decimal("2")) == Decimal("2")
    assert tax_round_up(Decimal("1.47")) == Decimal("1.50")


def test_is_imported():
    assert is_imported("Imported box of chocolates")
    assert not is_imported("Book")
    assert is_imported("box of imported chocolates")


def test_word_in_phrase():
    assert is_word_in_phrase("test", "This is a test suite")
    assert not is_word_in_phrase("book", "I'm reading the newspaper")
    assert is_word_in_phrase("Chocolate", "This is a box of chocolates")
    assert is_word_in_phrase("book", "Book of thruth")


def test_is_exempt():
    assert is_exempt("book")
    assert not is_exempt("bottle of perfume")
    assert is_exempt("box of chocolates")
    assert is_exempt("box of headache pills")


def test_row_tax_percentage():
    assert get_row_tax_percentage("Imported box of chocolates") == Decimal("0.05")
    assert get_row_tax_percentage("Book") == Decimal("0")
    assert get_row_tax_percentage("Imported bottle of perfume") == Decimal("0.15")
    assert get_row_tax_percentage("music CD") == Decimal(".1")

