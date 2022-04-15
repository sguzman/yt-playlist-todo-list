import functools
from typing import Callable, Dict, List, Set, Tuple

import yt_dlp


def compose(*functions):
    return functools.reduce(lambda f, g: lambda x: f(g(x)), functions,
                            lambda x: x)


def make_markdown_table(array):
    """ Input: Python list with rows of table as lists
               First element as header.
        Output: String to put into a .md file

    Ex Input:
        [["Name", "Age", "Height"],
         ["Jake", 20, 5'10],
         ["Mary", 21, 5'7]]
    """

    markdown = "\n" + str("| ")

    for e in array[0]:
        to_add = " " + str(e) + str(" |")
        markdown += to_add
    markdown += "\n"

    markdown += '|'
    for i in range(len(array[0])):
        markdown += str("-------------- | ")
    markdown += "\n"

    for entry in array[1:]:
        markdown += str("| ")
        for e in entry:
            to_add = str(e) + str(" | ")
            markdown += to_add
        markdown += "\n"

    return markdown + "\n"


def build_vid_url(s: str) -> str:
    return f'https://www.youtube.com/watch?v={id}'


def ydl_opts() -> Dict[str, str]:
    return {'format': 'bestaudio'}


A = str
Z = str


def init() -> A:
    import sys

    return sys.argv[1]


def pipe(f: Tuple[) -> Callable:
    def p(in_arg):
        out_arg = f(in_arg)
        print(n, in_arg, out_arg, f, sep='\n\t')

        return out_arg

    return p


def build_prog() -> Callable:
    prog: List[Callable] = [lambda x: (x, ydl_opts()), lambda x: x]
    wrap = list(map(pipe, prog))

    return compose(*wrap)


def main() -> None:
    print('hi')

    arg = init()
    prog = build_prog()
    prog(arg)
    print('bye')


if __name__ == '__main__':
    main()
