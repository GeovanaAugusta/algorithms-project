def study_schedule(permanence_period, target_time):

    count = 0

    if not target_time:
        return None

    if not all(all(isinstance(i, int) for i in tup)
               for tup in permanence_period):
        return None

    for first, second in permanence_period:
        if first <= target_time <= second:
            count += 1

    return count

# SOURCE
# 1
# Verificar se todos os itens de um array de tuplas tem o mesmo tipo
# https://stackoverflow.com/questions/13252333/check-if-all-elements-of-a-list-are-of-the-same-type
