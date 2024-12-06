#5. Предприятие может предоставить работу по одной специальности 4 женщинам, по другой - 6 мужчинам, по третьей - 3 работникам независимо от пола. 
# Сформировать все возможные варианты заполнения вакантных мест, если имеются 14 претендентов: 6 женщин и 8 мужчин.

import itertools
import timeit

# Данные:
women = 6  #
men = 8   
total = women + men  

# Специальности:
specialty1 = 4  # для первой специальности 4 женщины
specialty2 = 6  # для второй специальности 6 мужчин
specialty3 = 3  # для третьей специальности 3 работника (независимо от пола)

def algorithm():
    result = []
    for w in range(min(specialty1, women) + 1):
        for m in range(min(specialty2, men) + 1):
            for t in range(min(specialty3, total) + 1):
                if w <= women and m <= men and t <= (total - (w + m)):
                    result.append((w, m, t))
    return result

def pythonFunc():
    result = []
    for w in itertools.combinations(range(women), specialty1):
        for m in itertools.combinations(range(men), specialty2):
            for t in itertools.combinations(range(total), specialty3):
                if len(set(w).union(set(m))) <= women and len(set(t)) <= total:
                    result.append((w, m, t))
    return result


N = total  #общее количество претендентов

#algorithm
start_time_algo = timeit.default_timer()
algorithm = pythonFunc()
end_time_algo = timeit.default_timer()

#pythonFunc
start_time_func = timeit.default_timer() 
python_result = pythonFunc()
end_time_func = timeit.default_timer()


print(f"Вариантов (алгоритмический способ): {len(algorithm)}")
print(f"Время (алгоритмический способ): {end_time_algo - start_time_algo:.6f} секунд")

print(f"\nВариантов (функции Python): {len(python_result)}")
print(f"Время (функции Python): {end_time_func - start_time_func:.6f} секунд")


