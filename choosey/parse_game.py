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


def choose(name, stepdict):
    print(f'--({name})-->', stepdict['_text'])

    choices = {str(i): key for i, key in enumerate(stepdict.keys()) if key != '_text'}
    while True:
        for num, choice in choices.items():
            print(num, choice)

        response = input('choose a number: ')
        if response in choices:
            return stepdict[choices[response]]
        else:
            print('*** invalid choice, you dimwit! ***')


def play(gamedict):
    pprint.pprint(gamedict)
    step = 'step1'
    while True:
        step = choose(step, gamedict[step])


if __name__ == '__main__':
    game = read_game(sys.argv[1])
    # play(game)
    graph(game)
