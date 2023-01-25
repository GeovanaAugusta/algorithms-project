# Uma função que chama a si mesma é chamada de recursiva.
# O processo para executar tal função recursiva é chamado de recursividade.

def is_palindrome_recursive(word, low_index, high_index):
    # print(word)
    # print("low_index", low_index, "high_index", high_index)

    if not word or word == '':
        return False

    if word != word[::-1]:
        return False

    # print(low_index > high_index)
    if low_index > high_index:
        return True

    # print(is_palindrome_recursive(word, low_index + 1, high_index - 1))
    return is_palindrome_recursive(word, low_index + 1, high_index - 1)

# SOURCE
# 3
# https://www.mygreatlearning.com/blog/palindrome-in-python/
#  reversed_string == string[::-1]
