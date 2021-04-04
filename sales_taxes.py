import argparse

from data_feed import input1, input2, input3
from src.parser import parse_raw_input
from src.printer import print_output


def printer(input: str):
    if type(input) != str:
        raise TypeError("please provide a valid string as input")
    print("\nPrinting output elaborated from input:")
    print("------")
    print(input)
    print("------")
    output = print_output(parse_raw_input(input))
    print("Output")
    print("------")
    print(output, "\n")


parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group()
group.add_argument(
    "-i",
    "--input",
    type=int,
    choices=[1, 2, 3],
    help="get output using a predefined test input",
)
group.add_argument(
    "-s", "--string", type=str, help="get output from a custom string input"
)
args = parser.parse_args()

if args.input == 1:
    printer(input1)
elif args.input == 2:
    printer(input2)
elif args.input == 3:
    printer(input3)

if args.string:
    printer(args.string)

