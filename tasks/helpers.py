from os import popen


def print_header(header: str) -> None:
    cols = get_terminal_columns()
    prefix, sufix = build_separators(cols, header)
    head = build_head(prefix, header, sufix)

    print()
    print(head)
    print()


def get_terminal_columns() -> int:
    _, cols = popen("stty size", "r").read().split()

    return int(cols)


def build_separators(cols: int, header: str) -> tuple:
    char = "="
    header_len = len(header) + 2
    length = cols - header_len

    line = char * length
    middle = length // 2
    prefix, sufix = line[:middle], line[middle:]

    return prefix, sufix


def build_head(prefix: str, header: str, sufix: str) -> str:
    components = [prefix, header, sufix]

    return " ".join(components)
