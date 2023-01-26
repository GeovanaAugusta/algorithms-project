# 4.1 - Retorne True se as palavras passadas por parâmetro forem anagramas;

# 4.2 - Retorne False se as palavras passadas por parâmetro não forem;

# 4.3 - Retorne False se alguma das palavras passadas por parâmetro for '';

# 4.4 - Máximo O(n log n), ou seja, com complexidade assintótica linearítmica.

# 4.5 - Retorne True -> anagramas sem diferenciar maiúsculas e minúsculas.


def quick_sort(arr, low_index, high_index):
    if low_index < high_index:
        # arr[pi] agora está no lugar certo
        pi = partition(arr, low_index, high_index)

        # Antes e depois do pivô
        quick_sort(arr, low_index, pi - 1)
        quick_sort(arr, pi + 1, high_index)


def partition(arr, low_index, high_index):
    # Elemento para posicionar corretamente, um pivô pra comparar
    pivot = arr[high_index]

    # Index do menor elemento indica posição certa do pivô
    i = low_index - 1

    # j é o índice em que o pivo agora está.
    for j in range(low_index, high_index):

        # Se o elemento iterado é menor que o pivô, aumenta um no mesmo
        if arr[j] < pivot:

            i += 1

            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high_index] = arr[high_index], arr[i + 1]

    return i + 1


def ordenation(first_string_list_c_i, second_string_list_c_i):
    # print(quick_sort(first_string_list_c_i, 0,
    #       len(first_string_list_c_i) - 1))

    # De fato ordeno aqui, chamando a quick_sort
    quick_sort(first_string_list_c_i, 0,
               len(first_string_list_c_i) - 1)

    quick_sort(second_string_list_c_i, 0,
               len(second_string_list_c_i) - 1)


def array_to_string(array):
    word = ''

    for caracter in array:
        word += caracter

    # print(word)
    return word


def array_to_word(caract_arr):
    # Para que o loop não exceda o tamanho do array(1, len)
    for caracter in range(1, len(caract_arr)):
        key = caract_arr[caracter]
        print("key", key)
        # Um caractere antes, já que delimitei de 1 ao tamanho do array
        # previous_caracter é o índice em que o pivô agora está.
        previous_caracter = caracter - 1
        # Enquanto o índex do caractere anterior for >=0
        # E a chave vier antes da variável previous_caracter (c -1)
        # Evitando quebrar
        # Resumindo comparo o segundo elemento da lista com os anteriores,
        # e dessa forma fica na posição correta
        # print("[previous_caracter + 1]", [previous_caracter + 1])
        # print("caract_arr[previous_caracter]", caract_arr[previous_caracter])

        while (previous_caracter >= 0 and key
               < caract_arr[previous_caracter]):

            caract_arr[previous_caracter + 1] = caract_arr[previous_caracter]
            previous_caracter -= 1

        caract_arr[previous_caracter + 1] = key
        # print("key", key)

    word = ''

    for caracter in caract_arr:
        word += caracter

    # print(word)
    return word


def is_anagram(first_string, second_string):

    # Para comparar caracter por caracter preciso transformar em lista 1º
    # e case insensitive
    first_string_list_c_i = list(first_string.lower())
    second_string_list_c_i = list(second_string.lower())

    # Estrutura esperada no teste, '' para a não passada
    # ('', palavra_escrita_corretamente, False)
    if first_string == "":
        return ('', array_to_word(second_string_list_c_i),
                False)

    if second_string == "":
        return (array_to_word(first_string_list_c_i), '', False)

    ordenation(first_string_list_c_i, second_string_list_c_i)

    # print("aaaa", array_to_string(first_string_list_c_i),
    #       second_string_list_c_i)

    # Estrutura esperada no teste
    # (ordered_first_string, ordered_second_string, True/False)
    if (first_string_list_c_i != second_string_list_c_i):
        return (array_to_string(first_string_list_c_i),
                array_to_string(second_string_list_c_i),
                False)

    if (first_string_list_c_i == second_string_list_c_i):
        return (array_to_string(first_string_list_c_i),
                array_to_string(second_string_list_c_i),
                True)

# Preciso transformar em string de novo, a lista -> array_to_string
# E       AssertionError: assert (['a', 'd', 'e', 'p', 'r'], ['a', 'a', 'a',
# 'd', 'e', 'p', 'r'], False) == ('adepr', 'aaadepr', False)
# E         At index 0 diff: ['a', 'd', 'e', 'p', 'r'] != 'adepr'
# E         Full diff:
# E         - ('adepr', 'aaadepr', False)
# E         + (['a', 'd', 'e', 'p', 'r'], ['a', 'a', 'a', 'd', 'e', 'p', 'r'],
# False)

# SOURCE
# 4
# Uso do quickSort
# https://www.geeksforgeeks.org/quick-sort/
# https://lamfo-unb.github.io/2019/04/21/Sorting-algorithms/
# partition (arr[], low, high)
# {
#     // pivot (Element to be placed at right position)
#     pivot = arr[high];

#     i = (low – 1)  // Index of smaller element and indicates the
#     // right position of pivot found so far

#     for (j = low; j <= high- 1; j++){

#         // If current element is smaller than the pivot
#         if (arr[j] < pivot){
#             i++;    // increment index of smaller element
#             swap arr[i] and arr[j]
#         }
#     }
#     swap arr[i + 1] and arr[high])
#     return (i + 1)
# }

# quickSort(arr[], low, high) {

#     if (low < high) {

#         /* pi is partitioning index, arr[pi] is now at right place */

#         pi = partition(arr, low, high);

#         quickSort(arr, low, pi – 1);  // Before pi

#         quickSort(arr, pi + 1, high); // After pi

#     }

# }

# int main()
# {
#     int arr[] = { 10, 7, 8, 9, 1, 5 };
#     int n = sizeof(arr) / sizeof(arr[0]);
#     quickSort(arr, 0, n - 1);
#     cout << "Sorted array: \n";
#     printArray(arr, n);
#     return 0;
# }
# Utilize qualquer algoritmo que quiser (Selection sort, Insertion sort,
# Bubble sort, Merge sort, Quick sort ou TimSort)

# Palavra em lista
# https://www.freecodecamp.org/news/python-string-to-array-how-to-convert-text-to-a-list/
