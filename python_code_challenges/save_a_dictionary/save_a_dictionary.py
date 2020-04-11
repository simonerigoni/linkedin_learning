# Save and load a dictionary using a pickle file
# python save_a_dictionary.py


import pickle


def save_dictonary(dictionary, filepath):
    '''
    Save a dictionary into a pickle file

    Arguments:
        dictionary (dict): dictionary to save
        filepath (str): filepath to save the dictionary

    Returns
        None
    '''
    with open(filepath, 'wb') as output_file:
        pickle.dump(dictionary, output_file)


def load_dictonary(filepath):
    '''
    Load a dictionary from a file

    Arguments:
        filepath (str): filepath to save the dictionary

    Returns
        dictionary (dict): loaded dictionary
    '''
    dictonary = dict()
    with open(filepath, 'rb') as input_file:
        return pickle.load(input_file)


if __name__ == '__main__':
    save_dictonary({1 : 'pippo', 2 : 'pluto', 3 : 'paperino'}, 'disney_characters.pickle')
    print(load_dictonary('disney_characters.pickle'))