import random


def roll(times=1, sides=6):
    rolls = []
    for i in range(times):
        rolls.append(random.randint(1, sides))
    return rolls


def roll_attack(command='1d6'):
    times, sides = command.split('d')
    rolled = sum(roll(int(times), int(sides)))
    return rolled


if __name__ == '__main__':

    rolled, modifier = roll_attack(input('type dice roll here (example: 2d6+5): '))
    print(f'{rolled}+{modifier} = {rolled + modifier}')
