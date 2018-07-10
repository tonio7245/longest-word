import random
import string
import requests


class Game:
    def __init__(self):
        self.grid = []
        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word):
        if not word:
            return False
        letters = self.grid.copy() # Consume letters from the grid
        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        return self.verify_word_exist(word)

    def verify_word_exist(self,word):
        r = requests.get('https://wagon-dictionary.herokuapp.com/' + word)
        return r.json()['found']

