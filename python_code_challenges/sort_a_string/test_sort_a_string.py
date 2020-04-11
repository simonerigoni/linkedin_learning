# Test sort_words()
# pytest


from sort_a_string import sort_words


def test_sort_words():
    assert sort_words('a b c') == 'a b c'
    assert sort_words('Pippo is a word') == 'a is Pippo word'
    assert sort_words('banana ORANGE apple') == 'apple banana ORANGE'