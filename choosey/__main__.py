import sys
from pathlib import Path
import argparse

from choosey.parse_game import read_game, play, graph

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('--game', help="choose a game")
parser.add_argument('--graph', type=argparse.FileType('w'),
                    help="write a representation of the game as a graphviz graph and exit")
parser.add_argument('-s', '--start', default='START',
                    help="name of the step to start on (default %(default)s)")

args = parser.parse_args(sys.argv[1:])

topdir = Path(__file__).parent

if args.game:
    fname = next(topdir.rglob(f'*{args.game}*'))
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

if args.graph:
    args.graph.write(graph(game))
    sys.exit()

play(game, step=args.start)
