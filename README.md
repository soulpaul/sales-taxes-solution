# Sales Taxes Solution

This repo contains my solution to the [sales taxes problem](https://github.com/xpeppers/sales-taxes-problem)

## Requirements

- Python >=3.7
- Pytest

## Install

You may want to use a virtual environment of your choice and install requirements. For sake of simplicity I used venv

1. clone this repo: `git clone https://github.com/soulpaul/sales-taxes-solution.git` (if you haven't already done that)
2. `cd` into the folder in which you cloned this repo
3. create the virtual environment: `python3 -m venv .`
4. activate the virtual environment and install dependencies:

```bash
   source bin/activate
   pip install -r requirements.txt
```

## Assumptions

To elaborate this solution I made some assumptions based on the available data:

1. Exempt items are only the ones stated in the inputs. There is no mechanism in place to make the script understand if an item is food or a medicine if it's not used in the provided input. But a new exempt item or category can be easily added without breaking anything.
2. I expect input to be always a multiline string having a product for each row.
3. Each product in the input should be written using the price | name | "at" | price schema. Words are separated by spaces.
4. If a product is imported the product name in the output should always begin with "imported"

## Tests

By running `pytest` problem inputs -> expected outputs are tested as well. But you can also use verbose commands as stated in the **Usage** section

## Usage

You can check possible uses of the script in the CLI using:

```bash
python sales_taxes.py -h
```

To parse one of the input stated in the problem please use:

```bash
python sales_taxes.py -i {input-number}
```

ex. to check output 3 I would use:

```bash
python sales_taxes.py -i 3
```

You can provide custom string as well by using:

```bash
python sales_taxes.py -s "1 custom item at 12.99"
```
