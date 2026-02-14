cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers

    if 1 <= n <= 15:
        fibb = []
        for i in range(0, n):
            if i == 0:
                fibb.append(0)

            elif i == 1:
                fibb.append(1)

            else:
                new = fibb[-1] + fibb[-2]
                fibb.append(new)
        
        return(list(map(cube, fibb)))

    else: return "Error"

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
