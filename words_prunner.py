import argparse
from typing import List

def prune(words: List[str], min_length: int, max_unique_letters: int):
    words_prunned = get_min_length(words, min_length)
    words_prunned = remove_non_alpha(words_prunned)
    words_prunned = get_with_max_unique_letters(words_prunned, max_unique_letters)
    return words_prunned

def get_min_length(words: List[str], min_length: int = 4):
    return [w for w in words if len(w) >= min_length]

def remove_non_alpha(words: List[str]):
    set_alpha = set(list('abcdefghijklmnopqrstuvwxyz'))
    return [w for w in words if set(list(w.lower())) <= set_alpha]

def get_with_max_unique_letters(words: List[str], max_unique_letters: int = 7):
    return [w for w in words if len(set(list(w))) <= max_unique_letters]

def main():
    parser = argparse.ArgumentParser(description="Prune a list of words based on specified criteria.")
    parser.add_argument('--input_file', type=str, default='words.txt', help="The input file containing words.")
    parser.add_argument('--output_file', type=str, default='words_prunned.txt', help="The output file to write pruned words.")
    parser.add_argument('--min_length', type=int, default=4, help="The minimum length of words to keep.")
    parser.add_argument('--max_unique_characters', type=int, default=7, help="The maximum number of unique characters in words to keep.")
    
    args = parser.parse_args()
    
    with open(args.input_file, 'r') as f:
        words = f.read().splitlines()

    words_prunned = prune(words, args.min_length, args.max_unique_characters)

    with open(args.output_file, 'w+') as f:
        f.write("\n".join(words_prunned))

if __name__ == "__main__":
    main()
