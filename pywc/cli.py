import os, sys
from pathlib import Path


def get_number_of_bytes(file_name: Path):
    """
    Function to get the number of bytes in the file
    :param file_name: File name
    :return:
    """
    try:
        size = os.path.getsize(file_name)
        return size

    except FileNotFoundError:
        print(f"Error {file_name} not found", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"Error, {e}", file=sys.stderr)
        sys.exit(1)

def get_number_of_lines(file_name: Path):
    """
    Function to get the total number of lines in the file
    :param file_name:
    :return:
    """

    total_lines = 0

    try:
        with open(file_name, 'r', encoding="utf-8") as f:
            for line in f.readlines():
                total_lines += 1

        return total_lines

    except FileNotFoundError:
        print(f"Error {file_name} not found", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"{type(e)}Error, {e}", file=sys.stderr)
        sys.exit(1)

def count_words(file_name: Path):
    """
    Function to get the total number of words in the text file
    :param file_name:
    :return:
    """

    try:
        with open(file_name, 'r', encoding="utf-8") as f:
            words = f.read().split()

        return len(words)

    except FileNotFoundError:
        print(f"Error {file_name} not found", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"{type(e)}Error, {e}", file=sys.stderr)
        sys.exit(1)

def get_number_of_characters(file_name: Path):

    try:
        text = file_name.read_text(encoding="utf-8", errors="replace")

        return len(text)

    except FileNotFoundError:
        print(f"Error {file_name} not found", file=sys.stderr)
        sys.exit(1)

    except Exception as e:
        print(f"{type(e)}Error, {e}", file=sys.stderr)
        sys.exit(1)
