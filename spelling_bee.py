from typing import Set
import sys



class SpellingBee:
    main_letters: str
    letters: str
    words: Set[str]
    solution: Set[str]

    def __init__(self, main_letters: str, other_letters: str) -> None:
        self.letters = main_letters + other_letters
        self.main_letters = main_letters
        with open('words_prunned.txt', 'r') as f:
            self.words = set(f.read().lower().splitlines())
    
    def solve(self):
        words_with_main_letter = {w for w in self.words if set(self.main_letters) <= set(list(w))}
        words_with_only_valid_letters = {w for w in words_with_main_letter if set(list(w)) <= set(list(self.letters))}

        self.solution = words_with_only_valid_letters
    
    def display_words(self):
        print("\n".join(sorted(self.solution, key=lambda x: -len(x))))
    
    def generate_js(self, outfile='consoleSolver.js'):
        with open('consoleSolver.template.js', 'r') as f:
            code = f.read().replace('>PLACEHOLDER<', '\n'.join(self.solution))
        with open(outfile, 'w+') as f:
            f.write(code)

        return code

if len(sys.argv) < 3:
    print('Usage: {} main_letters other_letters'.format(sys.argv[0]))
    sys.exit(0)

main_letters, other_letters = sys.argv[1], sys.argv[2]
sb = SpellingBee(main_letters, other_letters)
sb.solve()
sb.display_words()
sb.generate_js()