# permanence_period = entrada e saída (1, 2)
# target_time = intervalo que quero a consulta

def study_schedule(permanence_period, target_time):

    count = 0

    if not target_time:
        return None

    if not all(all(isinstance(i, int) for i in tup)
               for tup in permanence_period):
        return None

    # Desestruturação no Python
    for first, second in permanence_period:
        # print("tup", first, second)
        # print("cond", first <= target_time <= second)
        if first <= target_time <= second:
            count += 1
    # print("count", count)
    return count
