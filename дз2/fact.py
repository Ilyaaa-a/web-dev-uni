def fact_it(n):
    if 1 <= n <= 10**5:
        numb = 1
        res = 1
        while numb <= n:
            res = res * numb
            numb += 1
        return res
    else: return "Error"

def fact_rec(n):
    if 1 <= n <= 10**5:
        if n == 1:
            return 1
        while n > 1:
            return n * fact_rec(n-1)
    else: return "Error"
    

if __name__ == "__main__":
    import time
    n = 900

    # Итерационный метод
    start = time.perf_counter()
    result_it = fact_it(n)
    time_it = time.perf_counter() - start

    # Рекурсивный метод
    start = time.perf_counter()
    result_rec = fact_rec(n)
    time_rec = time.perf_counter() - start
    
    print(f"n = {n}")
    print(f"Итерационный: {time_it:.10f} сек")
    print(f"Рекурсивный:  {time_rec:.10f} сек")
