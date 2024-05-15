This Python script solves the New York Times Spelling Bee puzzle. It provides more words than are accepted, but will usually generate a list of words containing all the words accepted by the puzzle.

# How to run

1. Ensure you have Python 3 installed.
1. Run `python3 spelling_bee.py '{middle letter}' '{other letters}'` file. e.g. `python3 spelling_bee.py 'a' 'qwerty'`.
The script will generate a JS file called `consoleSolver.js` that can be posted into the console on https://www.nytimes.com/puzzles/spelling-bee to solve the puzzle.

# words_prunner.py utility

`words_prunner.py` allows users to solve custom versions of the Spelling Bee, or use their own dictionary.

The list of words is prunned on:

* Minimum word length
* Maximum number of unique characters
* Remove words with non-alphabetic characters

## Usage

```bash
words_prunner --input_file words.txt --output_file words_prunned.txt --min_length 4 --max_unique_characters 7
```

## Arguments

* `--input_file`: Input file containing words
* `--output_file`: Output file to write pruned words
* `--min_length`: Minimum length of words to keep (default: 4)
* `--max_unique_characters`: Maximum number of unique characters in words to keep (default: 7)
