# Simulate dices
# python simulate_dice.py


from random import randint
from collections import Counter


def roll_dices(*dice, num_trials = 1000000):
    '''
    Get the probability of each value obatained by summing the values obtained by rolling a variable number of dices with a variable number of faces using a monte carlo simulation

    Arguments:
        *dice : a variable number of dices with a varable number of faces
        num_trials (int): number of trials. Default value 1000000

    Returns
        None
    '''
    counts = Counter()
    for roll in range(num_trials):
        counts[sum(randint(1, sides) for sides in dice)] += 1

    print('Outcome\tProbability')
    for outcome in range(len(dice), sum(dice) + 1):
        print('{}\t{:0.2f}%'.format(outcome, counts[outcome] * 100 / num_trials))


if __name__ == '__main__':
    roll_dices(6,6,4)