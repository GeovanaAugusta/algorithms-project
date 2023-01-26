def is_palindrome_iterative(word):

    if not word or word == '':
        return False

    return word == word[::-1]

