import time

def process_list(arr):
    
    if len(arr) > 10**3 or len(arr) < 1:
        return 'Error'
    
    result = []
    for i in arr:
        if i % 2 == 0:
            result.append(i**2)
        else:
            result.append(i**3)
    return result

def process_list_comp(arr):
    if len(arr) > 10**3 or len(arr) < 1:
        return 'Error'
    
    return [i**2 if i % 2 == 0 else i**3 for i in arr]

def process_list_gen(arr):
    if len(arr) > 10**3 or len(arr) < 1:
        yield "Error"
        return
    for i in arr:
        yield i**2 if i % 2 == 0 else i**3
        
if __name__ == '__main__':
    test_arr = list(range(1, 1001))

    start = time.perf_counter()
    res1 = process_list(test_arr)
    time1 = time.perf_counter() - start

    start = time.perf_counter()
    res2 = process_list_comp(test_arr)
    time2 = time.perf_counter() - start

    start = time.perf_counter()
    res3 = list(process_list_gen(test_arr))
    time3 = time.perf_counter() - start

    print(f"Обычный цикл:       {time1:.9f} сек")
    print(f"List comprehension: {time2:.9f} сек")
    print(f"Генератор:          {time3:.9f} сек")

    """
    
    Обычный цикл:      0.000132300 сек
    List comprehension: 0.000095000 сек
    Генератор:          0.000116400 сек
    
    """