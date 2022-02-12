import sys
import configparser
import pprint
import textwrap

import dice


def graphlabel(val, width):
    return '\n'.join(textwrap.wrap(val, width=width))


def nodename(val):
    return '_'.join(val.lower().split())


def graph(game, label_width=12):
    lines = ['digraph {']
    for step, d in game.items():
        fromname = nodename(step)
        nodelabel = graphlabel(step, width=label_width)
        lines.append(f'{fromname} [ label="{nodelabel}" ];')
        for key, val in d.items():
            if val in game:
                toname = nodename(val)
                edgelabel = graphlabel(key, width=label_width)
                lines.append(f'"{fromname}" -> "{toname}" [ label="{edgelabel}" '
                             f'color=grey fontcolor=grey];')

    lines.append('}\n')
    return '\n'.join(lines)


def read_game(fname):
    # see https://docs.python.org/3/library/configparser.html
    config = configparser.ConfigParser(empty_lines_in_values=False)
    config.read(fname)

    d = {section: dict(config[section]) for section in config.sections()}
    # pprint.pprint(d)
    return d


def combat(win=None, lose=None, ndice=2, to_win=7, **kwargs):
    rolls = dice.roll_amount(int(ndice))
    total = sum(rolls)
    print(f'You must roll {ndice}d6 and get at least {to_win} to win')
    input('press enter to roll the dice')
    print('you rolled: ')
    print(dice.draw_dice(rolls))
    if total >= int(to_win):
        print('you won!')
        return win
    else:
        print('you lost...')
        return lose


def choose(name, step):
    print(f'---[ {name} ]---\n', step['_text'])

    if '_action' in step:
        action = step['_action']
        return globals()[action](**step)

    choices = {str(i): key for i, key in enumerate(step.keys()) if key != '_text'}
    while True:
        for num, choice in choices.items():
            print(num, choice)

        response = input('choose a number: ')
        if response in choices:
            return step[choices[response]]
        else:
            print('*** invalid choice, you dimwit! ***')


def play(game, step='START'):
    #pprint.pprint(game)
    while True:
        step = choose(step, game[step])


if __name__ == '__main__':
    game = read_game('games/game1.ini')
    # play(game)
    play(game, 'prepare for the demon')
    # graph(game)
