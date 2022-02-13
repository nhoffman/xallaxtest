import sys
import configparser
import pprint
import textwrap
import random
import string

try:
    from . import actions
except ImportError:
    import actions


def graphlabel(val, width):
    return '\n'.join(textwrap.wrap(val, width=width))


def nodename(val):
    return '_'.join(val.lower().split())


def graph(game, label_width=12):
    lines = ['digraph {']
    for step, d in game.items():
        fromname = nodename(step)
        nodelabel = graphlabel(step, width=label_width)
        if '_action' in d:
            nodelabel += '\n[{}]'.format(d['_action'])

        lines.append(f'{fromname} [ label="{nodelabel}" ];')
        # if one of the options is '???', create a dummy node to connect to
        if '???' in d.values():
            dummy = ''.join(random.choices(string.ascii_letters, k=6))
            lines.append(f'{dummy} [ label="???" ];')

        for key, val in d.items():
            edgelabel = graphlabel(key, width=label_width)
            if val in game:
                toname = nodename(val)
                lines.append(f'"{fromname}" -> "{toname}" [ label="{edgelabel}" '
                             'color=grey fontcolor=grey];')
            elif val == '???':
                lines.append(f'"{fromname}" -> "{dummy}" [ label="{edgelabel}" '
                             'color=grey fontcolor=grey];')


    lines.append('}\n')
    return '\n'.join(lines)


def read_game(fname):
    # see https://docs.python.org/3/library/configparser.html
    config = configparser.ConfigParser(empty_lines_in_values=False)
    config.read(fname)

    d = {section: dict(config[section]) for section in config.sections()}
    # pprint.pprint(d)
    return d


def choose(name, step):
    print(f'---[ {name} ]---\n', step['_text'])

    args = {k: v for k, v in step.items() if not k.startswith('_')}
    action = step.get('_action', 'ask')
    return getattr(actions, action)(**args)


def play(game, step='START'):
    #pprint.pprint(game)
    while True:
        step = choose(step, game[step])


if __name__ == '__main__':
    game = read_game('games/game1.ini')
    # play(game)
    play(game, 'prepare for the demon')
    # graph(game)
