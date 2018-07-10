import unittest
import string
from game import Game

class TestGame(unittest.TestCase):
    def test_game_initialization(self):
        new_game = Game()
        grid = new_game.grid
        self.assertIsInstance(grid, list)
        self.assertEqual(len(grid), 9)
        for letter in grid:
            self.assertIn(letter, string.ascii_uppercase)

    def test_is_invalid(self):
        new_game = Game()
        grid = new_game.grid
        new_game.grid = ['B','R','O','U','I','L','L','E','R']
        self.assertFalse(new_game.is_valid('BOUYA'))

    def test_empty_is_invalid(self):
        new_game = Game()
        grid = new_game.grid
        new_game.grid = ['B','R','O','U','I','L','L','E','R']
        self.assertFalse(new_game.is_valid(''))

    def test_is_valid(self):
        new_game = Game()
        grid = new_game.grid
        new_game.grid = ['B','R','O','U','I','L','L','E','R']
        self.assertTrue(new_game.is_valid('BROUILLER'))

