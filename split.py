import argparse
from typing import Optional


def main(
    str_line: list[str], MAX_LINES: int, MAX_SIZE: int, NUMBER_OF_FILES: int
) -> list[list[str]]:
    if MAX_LINES:
        return split_by_line(str_line, MAX_LINES)
    elif MAX_SIZE:
        return split_by_size(str_line, MAX_SIZE)
    elif NUMBER_OF_FILES:
        return split_by_number(str_line, NUMBER_OF_FILES)


def split_by_line(str_line: list[str], MAX_LINES: int) -> list[list[str]]:
    output = []
    line_len = len(str_line)
    SPLIT_NUMBER = line_len // MAX_LINES
    ITER_NUMBER = (SPLIT_NUMBER + 1) if line_len % MAX_LINES != 0 else SPLIT_NUMBER

    for i in range(ITER_NUMBER):
        output.append(str_line[MAX_LINES * i : MAX_LINES * (i + 1)])

    return output


def split_by_size(str_line: list[str], MAX_SIZE: int) -> list[list[str]]:
    pass
    # TODO fill function


def split_by_number(str_line: list[str], NUMBER_OF_FILES: int) -> list[list[str]]:
    output = []
    MAX_LINES = len(str_line) // NUMBER_OF_FILES

    ITER_NUMBER = (MAX_LINES + 1) if len(str_line) % NUMBER_OF_FILES != 0 else MAX_LINES

    for i in range(ITER_NUMBER):
        output.append(str_line[MAX_LINES * i : MAX_LINES * (i + 1)])

        return output


if __name__ == "__main__":
    args = argparse.ArgumentParser(description="split file by line")
    args.add_argument("", dest="", help="file path", required=True)
    args.add_argument(
        "-o",
        "--output",
        help="output file name. You can use %n once to specify the orders",
    )
    args.add_argument("-l", "--max-line", help="max lines in one file")
    args.add_argument("-s", "--max-size", help="max size in one file")
    args.add_argument("-n", "--max-files", help="split file into {n} files")

    # TODO add arg parsing codes
    FILE_PATH: str = args.file_path
    OUTPUT_FILE_PATH: Optional[str] = None

    MAX_LINES: int = 2000
    MAX_SIZE = Optional[int] = None
    NUMBER_OF_FILES: Optional[int] = None

    if OUTPUT_FILE_PATH is None:
        OUTPUT_FILE_PATH = FILE_PATH

    IS_FORMAT_REQUIRED = FILE_PATH.find("%n")

    with open(FILE_PATH, "r") as opened_file:
        opened_file_str_list = opened_file.readlines()

    output_file_str_list = main(opened_file_str_list, MAX_LINES, MAX_SIZE, NUMBER_OF_FILES)

    with open(OUTPUT_FILE_PATH, "w") as output_file:
        output_file.writelines(output_file_str_list)
