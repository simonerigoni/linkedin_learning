# Test index_all_items
# pytest


from find_all_list_items import index_all_items


def test_index_all_items():
    assert index_all_items([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2) == [[0, 0, 1], [0, 1], [1, 1]]