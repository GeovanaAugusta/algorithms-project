def is_palindrome_iterative(word):

    # Retorne False se nenhuma palavra for passada como parâmetro
    if not word or word == '':
        return False

    return word == word[::-1]

# SOURCE
# 5
# https://www.mygreatlearning.com/blog/palindrome-in-python/
#  reversed_string == string[::-1]
