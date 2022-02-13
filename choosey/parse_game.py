
import configparser

try:
    from . import actions
except ImportError:
    import actions


def read_game(fname):
    # see https://docs.python.org/3/library/configparser.html
    config = configparser.ConfigParser(empty_lines_in_values=False)
    config.read(fname)

    d = {section: dict(config[section]) for section in config.sections()}
    # pprint.pprint(d)
    return d


def choose(name, step):
    print(f'\n---[ {name} ]---\n', step['_text'])

    args = {k: v for k, v in step.items() if not k.startswith('_')}
    action = step.get('_action', 'ask')
    return getattr(actions, action)(**args)


def play(game, step='START'):
    while True:
        step = choose(step, game[step])


if __name__ == '__main__':
    game = read_game('games/game1.ini')
    # play(game)
    play(game, 'prepare for the demon')
    # graph(game)
