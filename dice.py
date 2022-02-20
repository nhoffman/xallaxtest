import random


def roll(times=1, sides=6):
    rolls = []
    for i in range(times):
        rolls.append(random.randint(1, sides))
    return rolls


def roll_attack(command='1d6'):
    split_command = command.split('+')
    times, sides = split_command[0].split('d')
    rolled = (sum(roll(int(times), int(sides))))

    if len(split_command) == 2:
        modifier = int(split_command[1])
    else:
        modifier = 0
    return rolled, modifier


if __name__ == '__main__':

    rolled, modifier = roll_attack(input('type dice roll here (example: 2d6+5): '))
    print(f'{rolled}+{modifier} = {rolled + modifier}')
