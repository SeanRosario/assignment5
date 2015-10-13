import sys
sys.path.append("/home/ds-ga-1007/git/assignment5/sdr375/adventure")

from unittest import TestCase
from play import load_advent_dat
from game import Game

class CommandTest(TestCase):

    def setUp(self):
        game = Game()
        load_advent_dat(game)
        self.words = set(w.synonyms[0].text for w in game.vocabulary.values())
        self.words.remove('suspend')

    def test_intransitive_commands_should_not_throw_exceptions(self):
        for word in self.words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.do_command(['no'])  # WOULD YOU LIKE INSTRUCTIONS?
            game.do_command([word])

    def test_transitive_commands_should_not_throw_exceptions(self):
        for word in self.words:
            game = Game()
            load_advent_dat(game)
            game.start()
            game.do_command(['no'])  # WOULD YOU LIKE INSTRUCTIONS?
            game.do_command(['enter'])  # so we are next to lamp
            game.do_command([word, 'lamp'])

    def test_do_commands(self):
        yes_no_list= ["yes","y","no","n"]
        wrong_words= ["yea!", "Nope", "Noway", "You betcha", "^!@#$%^{}|}{}|~&*C"]
        for word in wrong_words:
            game = Game()
            load_advent_dat(game)
            game.yesno_callback = self.assertTrue
            game.start()
            game.do_command([word])
            
        for word in yes_no_list:
            game = Game()
            load_advent_dat(game)
            game.yesno_callback = self.assertTrue
            game.start()
            game.do_command([word])
        