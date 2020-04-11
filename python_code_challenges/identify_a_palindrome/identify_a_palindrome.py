# Identify if a word is palindrome
# python identify_a_palindrome.py


import re 


def is_palindrome(stringa):
    '''
    Returns True if the input string is palindrome and False otherwise. Not case sensitive and ignores spaces

    Arguments:
        stringa (string): input string

    Returns
        is_palindrome (boolean): True if the input string is palindrome and False otherwise
    '''
    clean_stringa = ''.join(re.findall(r'[a-z]+', stringa.lower()))
    backwards_clean_stringa = clean_stringa[::-1]
    return clean_stringa == backwards_clean_stringa

if __name__ == '__main__':
    print(is_palindrome('race car'))