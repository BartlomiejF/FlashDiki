# FlashDiki [![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE) 
CLI app that translate english words to polish, save chosen translations and create both printable and interactive flashcards.

# Description
The script translates words with www.diki.pl web translator and lists translations in your terminal. It is possible to save one of the listed translations in a .txt file and eventually create flashcards from saved translations.

# Installation
Simply download the repository files or using git

    git clone https://github.com/BartlomiejF/FlashDiki.git

Then install required packages with command

    python3 -m pip install -r requirements.txt

# Usage
### List translations of a word ("print" in the following case)

![translation only](/docs/gifs/diki_translate_base.gif)

### Save the translation with -a/--add <number-from-list>
    
    python3 main.py print -a 2
    
Adds the second translation from listed translations. If -a/--add with no number is provided then the first translation is added.

![add translation](/docs/gifs/add_translation.gif)

If there is no translations.txt file in the script folder then it is created right now.
    
### Print all of your saved translations with -p/--print

    python3 main.py -p
    
![print translations](/docs/gifs/diki_print.gif)

### Remove translation from saved translations with -r/--remove <number from list>
    
    python3 main.py -r 46
    
![remove translation](/docs/gifs/diki_remove.gif)

### If you have your own translation and would like to save it use -o/--own <translation> argument
    
    python3 main.py print -o bardzo dobre tłumaczenie
    
![diki add own translation](/docs/gifs/diki_own_translation.gif)

This automatically saves the translation.

### To create flashcards use -f/--flashcards argument

    python3 main.py -f
    
![create flashcards](/docs/gifs/diki_flashcards.gif)

Flashcards are stored in a folder named flashcards.

#### For your own convenience it is suggested to make an alias 

Add to your .bashrc or .bash_aliases the following line:
    
    alias <your command> = "python3 path/to/the/FlashDiki/folder/main.py"
    
# Have fun.

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
