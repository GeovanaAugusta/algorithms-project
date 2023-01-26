def validation(nums):
    visto = set()

    for num in nums:

        if num in visto:
            return num

        visto.add(num)


def verify_duplicate_num(nums):
    # Conto a repetição de números, n: x repetido
    duplicatas = dict((key, nums.count(key)) for key in nums)

    # Itero a dict de forma que se for menor que 2, a mesma é deletada
    for key in list(duplicatas):
        if duplicatas[key] < 2:
            del duplicatas[key]

    # print(duplicatas)

    # Por fim verifico se o tamanho da lista, agora só com valores
    # que se repetem + que 2x, tem 1 item apenas ou +1
    # Ter apenas um único número repetindo duas ou mais vezes
    if len(duplicatas) > 1:
        return False

    if len(duplicatas) == 1:
        print(len(duplicatas))
        print(validation(nums))
        return validation(nums)

    # Retorne False se a função receber como parâmetro uma lista
    # sem números repetidos
    return False


def find_duplicate(nums):

    nums.sort()

    #  Retorne False se a função não receber nenhum parâmetro
    # ou uma string
    if not nums or any(isinstance(x, str) for x in nums):
        return False

    # Retorne False se a função receber como parâmetro apenas um valor
    if len(nums) <= 1:
        return False

    # Retorne False se a função receber como parâmetro um número negativo
    if any(i < 0 for i in nums):
        return False

    return verify_duplicate_num(nums)


# SOURCE
# 5

# https://www.w3schools.com/python/ref_keyword_del.asp#:~:text=The%20del%20keyword%20is%20used,parts%20of%20a%20list%20etc.
# https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
# https://stackoverflow.com/questions/15993583/python-identify-a-negative-number-in-a-list
