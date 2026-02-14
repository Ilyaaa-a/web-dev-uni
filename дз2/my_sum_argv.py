import sys

def my_sum(numbers):
    return sum(numbers)

if __name__ == '__main__':
    args = [int(x) for x in sys.argv[1:]]
    result = my_sum(args)
    print(result)