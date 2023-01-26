def quick_sort(arr, low_index, high_index):
    if low_index < high_index:

        pi = partition(arr, low_index, high_index)


        quick_sort(arr, low_index, pi - 1)
        quick_sort(arr, pi + 1, high_index)


def partition(arr, low_index, high_index):
    pivot = arr[high_index]

    i = low_index - 1

    for j in range(low_index, high_index):

        if arr[j] < pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high_index] = arr[high_index], arr[i + 1]

    return i + 1


def ordenation(first_string_list_c_i, second_string_list_c_i):

    quick_sort(first_string_list_c_i, 0,
               len(first_string_list_c_i) - 1)

    quick_sort(second_string_list_c_i, 0,
               len(second_string_list_c_i) - 1)


def array_to_string(array):
    word = ''

    for caracter in array:
        word += caracter

    return word


def array_to_word(caract_arr):

    for caracter in range(1, len(caract_arr)):
        key = caract_arr[caracter]

        previous_caracter = caracter - 1
        

        while (previous_caracter >= 0 and key
               < caract_arr[previous_caracter]):

            caract_arr[previous_caracter + 1] = caract_arr[previous_caracter]
            previous_caracter -= 1

        caract_arr[previous_caracter + 1] = key

    word = ''

    for caracter in caract_arr:
        word += caracter
        
    return word


def is_anagram(first_string, second_string):


    first_string_list_c_i = list(first_string.lower())
    second_string_list_c_i = list(second_string.lower())

    if first_string == "":
        return ('', array_to_word(second_string_list_c_i),
                False)

    if second_string == "":
        return (array_to_word(first_string_list_c_i), '', False)

    ordenation(first_string_list_c_i, second_string_list_c_i)

    if (first_string_list_c_i != second_string_list_c_i):
        return (array_to_string(first_string_list_c_i),
                array_to_string(second_string_list_c_i),
                False)

    if (first_string_list_c_i == second_string_list_c_i):
        return (array_to_string(first_string_list_c_i),
                array_to_string(second_string_list_c_i),
                True)