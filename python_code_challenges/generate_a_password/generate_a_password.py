# Generate a passphrase
# python generate_a_password.py


import secrets


def generate_passphrase(number_of_words, diceware_wordlist):
    '''
    Generate a passphrase using diceware

    Arguments:
        number_of_words (int): number of words composing the passphrase

    Returns
        passphrase (str): passphrase generated
    '''
    value_word = dict()
    num_trials = 5
    sides = 6
    passphrase = []

    with open(diceware_wordlist, 'r') as input_file:
        lines = input_file.readlines()[2:7778] # lines ad top and at bottom do not contains the information we needs
        words = [line.split()[1] for line in lines]
        
    #print(words)

    passphrase = [secrets.choice(words) for i in range(number_of_words)]
        
    return ' '.join(passphrase)


if __name__ == '__main__':
    print(generate_passphrase(5, 'diceware_wordlist.asc'))