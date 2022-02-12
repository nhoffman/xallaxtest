try:
    from . import dice
except ImportError:
    import dice


def ask(**kwargs):
    choices = {str(i + 1): key for i, key in enumerate(kwargs.keys())}
    while True:
        for num, choice in choices.items():
            print(num, choice)

        response = input('choose a number: ')
        if response in choices:
            return kwargs[choices[response]]
        else:
            print('*** invalid choice, you dimwit! ***')


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


