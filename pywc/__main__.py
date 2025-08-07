from pathlib import Path
import argparse

from .cli import get_number_of_bytes, get_number_of_lines, count_words

def main():
    # Setting the Argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--bytes", action="store_true", help="Display number of bytes in a file.")
    parser.add_argument("-l", "--lines", action="store_true", help="Display number of lines in the file")
    parser.add_argument("file", type=str, help="Absolute path of the file")
    args = parser.parse_args()

    file = Path(args.file)

    if args.bytes:
        return get_number_of_bytes(file_name=file)

    if args.lines:
        return get_number_of_lines(file_name=file)

    return count_words(file_name=file)


if __name__ == "__main__":
    res = main()
    print(res)