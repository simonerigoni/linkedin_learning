# Get most used words from a file
# python count_unique_words.py


import re
from collections import Counter


def count_words(filepath, top_n = 20):
    '''
    Count the total number of words in a text file and get the n most frequent words and their number of occurrences

    Arguments:
        filepath (str): path of the input file
        top_n (int): how many top words to consider. Default value 20

    Returns
        None
    '''
    with open(filepath, 'r') as input_file:
        content = input_file.read()
        words = re.findall(r"[0-9a-zA-Z-']+", content)
        words_lower = [word.lower() for word in words]
        total_words = len(words_lower)

        word_counts = Counter()
        for word in words_lower:
            word_counts[word] += 1

        if total_words < top_n:
            top_n = total_words

        print('Total words: {}\nTop {} words:'.format(total_words, top_n))
        for word in word_counts.most_common(top_n):
            print('{} : {}'.format(word[0], word[1]))


if __name__ == '__main__':
    count_words('text_file.txt')