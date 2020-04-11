# Get a list on indeces of the searched itme in the input list
# python find_all_list_items.py


def index_all_items(lista, item):
    '''
    Get a list on indeces of the searched itme in the input list. The function also handles multidimensional lists

    Arguments:
        lista (list): input list
        item (int): searched item

    Returns
        indeces (list): list on indeces of the searched item in the input list
    '''
    indeces = []
    for i in range(len(lista)):
        if lista[i] == item:
            indeces.append([i])
        elif isinstance(lista[i], list):
            for index in index_all_items(lista[i], item):
                indeces.append([i] + index)
    return indeces


if __name__ == '__main__':
    print(index_all_items([[[1, 2, 3], 2, [1, 3]], [1, 2, 3]], 2))