def my_sum(*numbers):
    res = 0
    for i in numbers:
        res += i

    return res

print(my_sum(3,1,2))