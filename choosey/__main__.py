import sys
from pathlib import Path

from choosey.parse_game import read_game, play, graph

topdir = Path(__file__).parent

if sys.argv[1:]:
    name = sys.argv[1]
    fname = next(topdir.rglob(f'*{name}*'))
    print(fname)
else:
    print('choose a game')
    games = list((topdir / 'games').rglob('*.ini'))
    choices = {str(i + 1): game for i, game in enumerate(games)}

    while True:
        for num, game in choices.items():
            print(num, game)
        choice = input('pick a number: ')
        if num in choices:
            fname = choices[num]
            break


game = read_game(fname)
play(game)
