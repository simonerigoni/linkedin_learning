# Test is_palindrome()
# pytest


from identify_a_palindrome import is_palindrome


def test_is_palindrome():
    assert is_palindrome('pippo') == False
    assert is_palindrome('aabbaa') == True
    assert is_palindrome('level') == True
    assert is_palindrome('race car') == True
    assert is_palindrome('Go hang a salami - I''m a lasagna hog') == True