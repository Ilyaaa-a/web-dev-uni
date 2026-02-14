def minion_game(string):
    vowels = "AEIOU"
    kevin_score = 0
    stuart_score = 0
    n = len(string)

    if (0 < n <= 10**6):
    
        for i in range(n):
            if string[i] in vowels:
                kevin_score += n - i
            else:
                stuart_score += n - i
        
        if kevin_score > stuart_score:
            print("Кевин", kevin_score)
        elif stuart_score > kevin_score:
            print("Стюарт", stuart_score)
        else:
            print("Ничья")
    else: print('Error')

if __name__ == '__main__':
    s = input().strip()
    minion_game(s)