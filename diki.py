import random
import itertools
from jinja2 import FileSystemLoader, Environment


def print_translations(filepath):
    """Print saved translations

    Args:
        filepath (pathlib.Path): path to the file that stores saved
        translations
    """
    print(f"\n{20*'*'} List of your translations {20*'*'}\n")
    with open(f"{filepath}", "r") as f:
        for n, meaning in enumerate(f.readlines()):
            print(n+1, meaning.strip())


def remove(filepath, num):
    with open(f"{filepath}", "r+") as f:
        file_contents = f.readlines()
        removed = file_contents.pop(num)
        f.seek(0)
        f.truncate()
        for translation in itertools.chain().from_iterable(file_contents):
            f.write(translation)
    print(f"Removed translation: {removed.strip()}")


def add_translation(filepath, word_eng, word_pol):
    with open(f"{filepath}", "a") as f:
        f.write(f"{word_eng} - {word_pol}\n")
        print(f"\nAdded translation {word_eng} - {word_pol}")


def create_flashcards(filepath,):
    with open(f"{filepath}", "r") as f:
        raw_words = f.readlines()

    file_loader = FileSystemLoader(f"{filepath.parent}/templates")
    env = Environment(loader=file_loader)
    template_printable = env.get_template("printable.html")
    template_interactive = env.get_template("interactive.html")

    words_temp = [x.split('-') for x in raw_words]
    words = [[x[0].strip(), x[1].strip()] for x in words_temp if len(x) > 1]
    rev_wrds = [[x[1].strip(), x[0].strip()] for x in words_temp if len(x) > 1]

    output_printable = template_printable.render(wordlist=words)
    random.shuffle(words)
    output_interactive = template_interactive.render(wordlist=words)
    random.shuffle(rev_wrds)
    output_interactive_rev = template_interactive.render(wordlist=rev_wrds)

    with open(f"{filepath.parent}/flashcards/printable.html", "w") as f:
        f.write(output_printable)
    with open(f"{filepath.parent}/flashcards/interactive.html", "w") as f:
        f.write(output_interactive)
    with open(f"{filepath.parent}/flashcards/interactive_rev.html", "w") as f:
        f.write(output_interactive_rev)

    print("Flashcards created.")
