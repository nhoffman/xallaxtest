
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
    return d


def perform_action(game_data, step_data):
    args = {k: v for k, v in step_data.items() if not k.startswith('_')}
    action = step_data.get('_action', 'ask')
    return getattr(actions, action)(game_data, **args)


def play(game, step_name='START'):
    # initialize a dictionary to hold the game state
    game_data = {
        'health': 10,
        'strength': 2,
        'inventory': {'candle', 'sword'},
    }
    while True:
        step_data = game[step_name]
        print(f'\n---[ {step_name} ]---\n', step_data['_text'])
        step_name = perform_action(game_data, step_data)


if __name__ == '__main__':
    game = read_game('games/game1.ini')
    # play(game)
    play(game, 'prepare for the demon')
