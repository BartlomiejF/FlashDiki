from bs4 import BeautifulSoup
import re
import requests
import itertools
import argparse
import pathlib
# import typing

import diki


def translate(word: str) -> list:
    """Translate word

    Arguments:
        word {str} -- the word to be translated

    Returns:
        [list] -- list of translations
    """
    req = requests.get(f"https://www.diki.pl/slownik-angielskiego?q={word}")
    page = BeautifulSoup(req.text, "html.parser")
    find_li = page.find_all("li", re.compile("meaning*"))
    find_a = [x.find_all("a", "plainLink") for x in find_li]
    flatten = itertools.chain().from_iterable(find_a)
    translated: list = [x.text for x in flatten]
    return translated


if __name__ == "__main__":
    filepath = pathlib.Path(__file__)
    translations_file = filepath.parent/"translated.txt"

    parser = argparse.ArgumentParser(
        description="""Translate english words to polish ones. The script connects
        to https://www.diki.pl/ to obtain the translation"""
        )

    parser.add_argument("word", nargs="*", default=None, type=str,
                        help="the word to be translated")

    parser.add_argument(
        "-a",
        "--add",
        help="add translation number nb to the file",
        metavar="nb",
        nargs="?",
        const=1,
        default=0,
        type=int
        )

    parser.add_argument("-p", "--print", action="store_true",
                        help="print your saved words")

    parser.add_argument(
        "-r",
        "--remove",
        help="if present, remove translation number nb from the saved\
            translations",
        type=int,
        default=0,
        metavar="nb",
    )

    parser.add_argument(
        "-o",
        "--own",
        help="",
        nargs="+",
    )

    parser.add_argument(
        "-f",
        "--flashcards",
        help="create flashcards",
        nargs="?",
        const=1,
    )

    args = parser.parse_args()
    if args.word:
        to_translate = " ".join(args.word)
        if args.own:
            own_translation = " ".join(args.own)
            diki.add_translation(
                translations_file,
                to_translate,
                own_translation,
                )
        else:
            translated = translate("+".join(args.word))
            if translated:
                for n, meaning in enumerate(translated):
                    print(n+1, meaning)
                if args.add:
                    diki.add_translation(
                        translations_file,
                        to_translate,
                        translated[args.add-1],
                        )
            else:
                print(f"{to_translate.capitalize()} has no translation.")

    if args.print:
        diki.print_translations(translations_file)

    if args.remove > 0:
        diki.remove(translations_file, args.remove-1)

    if args.flashcards:
        diki.create_flashcards(translations_file)
