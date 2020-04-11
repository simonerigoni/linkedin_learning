# Test get_prime_factors()
# pytest


from find_prime_factors import get_prime_factors


def test_get_prime_factors():
    assert get_prime_factors(2) == [2]
    assert get_prime_factors(13) == [13]
    assert get_prime_factors(630) == [2, 3, 3, 5, 7]