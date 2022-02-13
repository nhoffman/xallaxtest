"""Functions defining game actions.

* Every function must accept 'game_data' as the first argument, and must end
  with **kwargs to prevent errors if extra arguments are provided.
* Functions must return a string representing a key in the game dictionary.

"""

import pprint

try:
    from . import dice
except ImportError:
    import dice

def clear_screen():
    print('\n' * 50)


def ask(game_data, **kwargs):
    choices = {str(i + 1): key for i, key in enumerate(kwargs.keys())}

    while True:
        for num, choice in choices.items():
            print(f'{num}: {choice}')
        print('-' * 20)
        print('i: show character information')

        response = input('choose a number: ')
        if response in choices:
            clear_screen()
            return kwargs[choices[response]]
        elif response == 'i':
            print('character information:')
            for k, v in game_data.items():
                print('', k, v)
            input('press return to continue ')
            clear_screen()
        else:
            print('*** invalid choice, you dimwit! ***')


def combat(game_data, win=None, lose=None, ndice=2, to_win=7, **kwargs):
    rolls = dice.roll_amount(int(ndice))
    total = sum(rolls)
    print(f'You must roll {ndice}d6 and get at least {to_win} to win')
    input('Press enter to roll the dice. ')
    print('you rolled: ')
    print(dice.draw_dice(rolls))
    if total >= int(to_win):
        print('you won!')
        return win
    else:
        print('you lost...')
        return lose


