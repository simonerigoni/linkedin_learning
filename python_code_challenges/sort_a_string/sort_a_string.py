# Get the input phrase sorted in alphbeticaly order by word
# python sort_a_string.py


def sort_words(phrase):
    '''
    Get the input phrase sorted alphbeticaly order by word. Not case sensitive only for sorting and space is the word separator

    Arguments:
        phrase (string): input phrase

    Returns
        sorted_phrase (string): phrase with words sorted alphbeticaly
    '''
    splitted_phrase = phrase.split(' ')
    lower_splitted_phrase = [word.lower() for word in splitted_phrase]
    lower_splitted_phrase.sort()
    sorted_phrase = []

    for word_lower in lower_splitted_phrase:
        for word in splitted_phrase:
            if word_lower == word.lower():
                sorted_phrase.append(word)
    
    return ' '.join(sorted_phrase)


if __name__ == '__main__':
    print(sort_words('banana ORANGE apple'))