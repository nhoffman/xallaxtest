import sys
from pathlib import Path
import argparse
import subprocess

from choosey.parse_game import read_game, play
from choosey.graph import graph

parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter)
parser.add_argument('--game', help="choose a game")
parser.add_argument('--graph', action='store_true', default=False,
                    help="make a cool graphviz graph (svg) and open in Safari")
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
    stem = str(Path(fname).stem)
    dotfile = stem + '.dot'
    svgfile = f'{stem}.svg'

    with open(dotfile, 'w') as f:
        f.write(graph(game))

    subprocess.run(['dot', '-Tsvg', dotfile, f'-o{svgfile}'])
    print(f'wrote {svgfile}')
    subprocess.run(['open', '-a', 'Safari.app', svgfile])

    sys.exit()

play(game, step_name=args.start)
