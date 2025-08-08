from pathlib import Path
import argparse

from pywc.cli import (get_number_of_bytes,
                  get_number_of_lines,
                  count_words,
                  get_number_of_characters
                  )

def main():
    # Setting the Argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--bytes", action="store_true", help="Display number of bytes in a file.")
    parser.add_argument("-l", "--lines", action="store_true", help="Display number of lines in the file")
    parser.add_argument("-w", "--words", action="store_true", help="Display number of words in the file")
    parser.add_argument("-m", "--chars", action="store_true", help="Display number of characters in the file")
    parser.add_argument("file", type=str, help="Absolute path of the file")
    args = parser.parse_args()

    file = Path(args.file)

    # Check if there is are no flags passed
    if not any([args.bytes, args.lines, args.words, args.chars]):
        args.bytes = args.lines = args.words = args.chars = True

    # Check if the bytes flag is passed
    if args.bytes:
        print(get_number_of_bytes(file_name=file), end=" ")

    # Check if the lines flag is passed
    if args.lines:
        print(get_number_of_lines(file_name=file), end=" ")

    # Check if the words flag is passed
    if args.words:
        print(count_words(file_name=file), end=" ")

    # Check if the chars flag is passed
    if args.chars:
        print(get_number_of_characters(file_name=file), end=" ")


if __name__ == "__main__":
    main()