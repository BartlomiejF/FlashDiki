# FlashDiki [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) 
CLI app that translate english words to polish, save chosen translations and create both printable and interactive flashcards.

# Description
The script translates words with www.diki.pl web translator and lists translations in your terminal. It is possible to save one of the listed translations in a .txt file and eventually create flashcards from saved translations.

# Installation
Simply download the repository files or using git:

    git clone https://github.com/BartlomiejF/FlashDiki.git

Then install required packages with command:

    python3 -m pip install -r requirements.txt

# Usage
List translations of a word ("print" in the following case):

![translation only](/docs/gifs/diki_translate_base.gif)

Save the translation with -a/--add <number-from-list>:
    
    python3 main.py print -a 2
    
Adds the second translation from listed translations. If -a/--add with no number is provided then the first translation is added.

![add translation](/docs/gifs/add_translation.gif)
    
