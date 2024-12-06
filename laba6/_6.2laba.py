import itertools
import timeit


women = 6  
men = 8    
total = women + men  

# Специальности:
s1 = 4  # 4 женщины
s2 = 6  # 6 мужчин
s3 = 3  # 3 работника (независимо от пола)

def algorithm():
    result = []
    for w in range(min(s1, women) + 1):
        for m in range(min(s2, men) + 1):
            for t in range(min(s3, total) + 1):
                if w <= women and m <= men and t <= (total - (w + m)):
                    if (w + m + t) <= total:
                        result.append((w, m, t))
    return result


def pythonF():
    result = []
    for w in itertools.combinations(range(women), s1):
        for m in itertools.combinations(range(men), s2):
            for t in itertools.combinations(range(total), s3):
                if len(set(w).union(set(m))) <= women and len(set(t)) <= total:
                    if (len(w) + len(m) + len(t)) <= total:
                        result.append((w, m, t))
    return result

start_time_algo_opt = timeit.default_timer()
algo_result = algorithm()
end_time_algo_opt = timeit.default_timer()

start_time_func_opt = timeit.default_timer()
python_result = pythonF()
end_time_func_opt = timeit.default_timer()

# Вывод оптимизированных результатов
print(f"оптимизированных вариантов (алгоритмический): {len(algo_result)}")
print(f"время: {end_time_algo_opt - start_time_algo_opt:.6f} секунд")

print(f"\nоптимизированных вариантов (функции питон): {len(python_result)}")
print(f"Время: {end_time_func_opt - start_time_func_opt:.6f} секунд")

