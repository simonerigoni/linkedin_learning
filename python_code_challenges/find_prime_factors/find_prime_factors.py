# Get a list of prime factors of the given number
# python find_prime_factors.py


def get_prime_factors(number):
    '''
    Get a list of prime factors of the given number

    Arguments:
        number (int): input number

    Returns
        prime_factors (list): list of prime factors of the given number
    '''
    prime_factors = []
    divisor = 2

    while divisor <= number:
        if (number % divisor) == 0:
            prime_factors.append(divisor)
            number = number / divisor
        else:
            divisor = divisor + 1
    return prime_factors


if __name__ == '__main__':
    print(get_prime_factors(630))