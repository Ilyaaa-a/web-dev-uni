import re

def fun(s):
    # ровно один '@'
    if s.count('@') != 1:
        return False
    
    username, rest = s.split('@')
    
    # отя бы одна ., и после'@
    if '.' not in rest:
        return False
    
    # последняя точка
    last_dot_index = rest.rfind('.')
    website = rest[:last_dot_index]
    extension = rest[last_dot_index + 1:]
    
    if not username or not website or not extension:
        return False
    
    # Проверка username: только буквы, цифры, '-', '_'
    if not all(c.isalnum() or c in '-_' for c in username):
        return False
    
    # Проверка website: только буквы и цифры
    if not all(c.isalnum() for c in website):
        return False
    
    # Проверка extension: только буквы и длина <= 3
    if not (1 <= len(extension) <= 3):
        return False
    if not all(c.isalpha() for c in extension):
        return False
    
    return True


def filter_mail(emails):
    return list(filter(fun, emails))

if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

    filtered_emails = filter_mail(emails)
    filtered_emails.sort()
    print(filtered_emails)