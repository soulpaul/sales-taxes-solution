from collections import namedtuple
from decimal import *

Elaborated_Row = namedtuple("Elaborated_Row", "qty product price net_total tax")

TAX_EXEMPT_ITEMS = [
    # list of all the exempt items. Plurals not containing substring of singular item should be listed as well
    # FOODS
    "chocolate",
    # MEDICINES
    "headache pill",
    # BOOKS
    "book",
]


def format_two_decimal_places(amount: Decimal):
    return amount.quantize(Decimal("0.01"))


def tax_round_up(amount: Decimal):
    return (format_two_decimal_places(amount) * 2).quantize(
        Decimal(".1"), rounding=ROUND_UP
    ) / 2


def is_word_in_phrase(word: str, string: str):
    """Not case sensitive"""
    return f"{word.lower()}" in f"{string.lower()}"


def is_imported(product_name: str):
    return is_word_in_phrase("imported", product_name)


def is_exempt(product_name: str):
    search_result = [is_word_in_phrase(word, product_name) for word in TAX_EXEMPT_ITEMS]
    return True in search_result


def get_row_tax_percentage(product_name: str):
    exempt = is_exempt(product_name)
    imported = is_imported(product_name)
    if exempt and imported:
        return Decimal(".05")
    elif exempt and not imported:
        return Decimal("0")
    elif imported:
        return Decimal(".15")
    else:
        return Decimal(".1")


def get_elaborated_row(parsed_input: tuple):
    net_total = parsed_input.price * parsed_input.qty
    return Elaborated_Row(
        qty=parsed_input.qty,
        product=parsed_input.product,
        price=parsed_input.price,
        net_total=net_total,
        tax=parsed_input.qty
        * tax_round_up(
            parsed_input.price * get_row_tax_percentage(parsed_input.product)
        ),
    )


def row_mapper(row: tuple):
    return get_elaborated_row(row)


def print_output(parsed_input: tuple):
    elaborated_rows = tuple(map(row_mapper, parsed_input))
    sales_taxes = format_two_decimal_places(sum((row.tax) for row in elaborated_rows))
    total = format_two_decimal_places(
        sum((row.net_total + row.tax) for row in elaborated_rows)
    )
    list_of_strings = [
        f"{row.qty} {row.product}: {row.net_total + row.tax}" for row in elaborated_rows
    ]
    list_of_strings.append(f"Sales Taxes: {sales_taxes}")
    list_of_strings.append(f"Total: {total}")
    return "\n".join(list_of_strings)

