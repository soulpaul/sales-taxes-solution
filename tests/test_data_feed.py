import pytest

from ..data_feed import input1, input2, input3, output1, output2, output3
from ..src.printer import print_output
from ..src.parser import parse_raw_input


def test_sales_taxes_outputs():
    assert print_output(parse_raw_input(input1)) == output1
    assert print_output(parse_raw_input(input2)) == output2
    assert print_output(parse_raw_input(input3)) == output3

