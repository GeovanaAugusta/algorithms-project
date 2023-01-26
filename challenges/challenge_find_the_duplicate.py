def find_duplicate(nums):

    nums.sort()

    #  Retorne False se a função não receber nenhum parâmetro
    # ou uma string:
    # Retorne False se a função receber como parâmetro apenas um valor
    if len(nums) <= 1 or any(isinstance(x, str) for x in nums) is True:
        return False

    # Retorne False se a função receber como parâmetro um número negativo
    if any(i < 0 for i in nums):
        return False

    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return nums[i]

    return False

# SOURCE
# 5

# https://www.w3schools.com/python/ref_keyword_del.asp#:~:text=The%20del%20keyword%20is%20used,parts%20of%20a%20list%20etc.
# https://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string
# https://stackoverflow.com/questions/15993583/python-identify-a-negative-number-in-a-list
