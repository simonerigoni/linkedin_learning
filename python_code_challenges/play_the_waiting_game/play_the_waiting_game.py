# Plat the waiting game: to win the user has to press Enter exactly in time
# python play_the_waiting_game.py


import random
import time


def waiting_game():
    '''
    Waiting game: the function will ask the user to wait a random amount of seconds before pressing Enter. To win the user has to press Enter exactly in time

    Arguments:
        None

    Returns
        None
    '''
    waiting_time = random.randint(1, 5)
    print('Your target time is {} seconds'.format(waiting_time))
    input('Press Enter to begin')
    start_time = time.time()
    input('Press Enter again afetr {} seconds'.format(waiting_time))
    stop_time = time.time()
    elapsed_time = stop_time - start_time
    print('Elapsed time {:.2f}'.format(elapsed_time))
    if elapsed_time == waiting_time:
        print('You win!')
    elif elapsed_time > waiting_time:
            print('You lose! {:.2f} seconds too slow'.format(elapsed_time - waiting_time))
    elif elapsed_time < waiting_time:
            print('You lose! {:.2f} seconds too fast'.format(waiting_time - elapsed_time))


if __name__ == '__main__':
    waiting_game()