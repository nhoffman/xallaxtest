import random

def roll():
    return random.choice([1, 2, 3, 4, 5, 6])

def gamble():

    my_roll = roll()
    if my_roll > 4:
        goodness = 'GOOD'
        punct = '!'
    elif my_roll > 2:
        goodness = 'OK'
        punct = '.'
    else:
        goodness = 'BAD'
        punct = '...'

    print(f'your roll is {goodness}, it is a {my_roll}{punct}')


# for i in range(10):
#     gamble()

def scores():
    rolls = []
    for i in range(4):
        rolls.append(roll())
    print(rolls)

def scores():
    rolls = [roll() for i in range(4)]
    keep = sorted(rolls)[1:]
    return sum(keep)


# print([scores() for i in range(6)])

def a_mod():
    ability = scores()
    if ability >= 18:
        mod = 4
    elif ability >= 16:
        mod = 3
    elif ability >= 14:
        mod = 2
    elif ability >= 12:
        mod = 1
    elif ability >= 10:
        mod = 0
    elif ability >= 8:
        mod = -1
    elif ability >= 6:
        mod = -2
    elif ability >= 4:
        mod = -3
    else:
        mod = -4

    return ability, mod

 #abilities = sorted([a_mod() for i in range(6)], reverse=True)

#for score, mod in abilities:
 #   print(f'score: {score} ({mod})')


scores = [scores(), scores(), scores(), scores(), scores(), scores()]
# scores = [scores() for i in range(6)]

races = dict(elf=[0, 2, 0, 0, 0, 0])
print('list of races:')
for race in races.keys():
    print(race)

print('your scores are', scores)
abilities = {}
for a_scores in scores:
    answer = input(f'choose which ability you want for this score: {a_scores}')
    abilities[answer] = a_scores
    print(abilities)

# answer = input('what is your race? ')
# print(f'ability score bonuses: {races[answer]}')




# pick = input('choose a ability for this score: 'scores)
# if pick == 'str':
#     print('is now your strength ability score!')
# elif pick == 'dex':
#     f
# elif pick == 'con':
#     f
# elif pick == 'int':
#     f
# elif pick == 'wis':
#     f
# elif pick == 'cha':
#     f
