import sys
import configparser
import pprint


def graph(game):
    lines = ['digraph {']
    for step, d in game.items():
        label = d.pop('_text')
        lines.append(f'{step} [label="{label}"];')
        for key, val in d.items():
            lines.append(f'{step} -> {val} [ label="{key}" ];')

    lines.append('}')
    print('\n'.join(lines))


def read_game(fname):
    # see https://docs.python.org/3/library/configparser.html
    config = configparser.ConfigParser(empty_lines_in_values=False)
    config.read(fname)

    d = {section: dict(config[section]) for section in config.sections()}
    # pprint.pprint(d)
    return d


def combat(win=None, lose=None, roll='2d6', to_win=7, **kwargs):
    print(f'You must roll {roll} and get at least {to_win} to win')
    input('press enter to roll the dice')
    print('you rolled a 9, you win!')
    return win


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


def play(gamedict, step='START'):
    while True:
        step = choose(step, gamedict[step])


if __name__ == '__main__':
    game = read_game(sys.argv[1])
    play(game, 'prepare for the demon')
    # graph(game)
