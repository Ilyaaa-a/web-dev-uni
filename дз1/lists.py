N = int(input().strip())

arr = []

for i in range(N):
    command = input().strip()

    if "insert" in command:
        command_arr = command.split()
        i_index = int(command_arr[1])
        e = int(command_arr[2])

        arr.insert(i_index, e)
    
    elif "print" in command:
        print(arr)

    elif "remove" in command:
        command_arr = command.split()
        e = int(command_arr[1])

        arr.remove(e)

    elif "append" in command:
        command_arr = command.split()
        e = int(command_arr[1])

        arr.append(e)

    elif "sort" in command:
        arr.sort()

    elif "pop" in command:
        arr.pop()

    elif "reverse" in command:
        arr.reverse()

# 1. insert i e: вставить целое число e в позицию i.

# 2. print: вывести список.

# 3. remove e: удалить первое вхождение целого числа e.

# 4. append e: вставить целое число e в конце списка.

# 5. sort: сортировать список.

# 6. pop: удалить последний элемент из списка.

# 7. reverse: перевернуть список.