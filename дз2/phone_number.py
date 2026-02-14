def wrapper(f):
    def fun(l):
        # complete the function
        formatted_numbers = []
        for number in l:
            # оставляем только цифры
            digits = ''.join(filter(str.isdigit, number))
            # берём последние 10 цифр
            if len(digits) >= 10:
                last_10 = digits[-10:]
            else:
                # на всякий случай нулями заполняем до 10 цифр
                last_10 = digits.zfill(10)[-10:]
            
            # форматируем
            formatted = f"+7 ({last_10[:3]}) {last_10[3:6]}-{last_10[6:8]}-{last_10[8:10]}"
            formatted_numbers.append(formatted)
        
        return f(formatted_numbers)
    return fun

@wrapper
def sort_phone(l):
    return sorted(l)

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    print(*sort_phone(l), sep='\n')
