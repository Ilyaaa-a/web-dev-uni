import os

def search_file(filename):
    # filename = input().strip()
    start_dir = os.path.dirname(os.path.abspath(__file__))  # папка, где этот файл
    
    found_path = None
    
    for root, dirs, files in os.walk(start_dir):
        if filename in files:
            found_path = os.path.join(root, filename)
            break  # только первый файл
    
    res = []

    if found_path:
        with open(found_path, 'r', encoding='utf-8') as f:
            for i, line in enumerate(f):
                if i >= 5:
                    break
                res.append(line.rstrip('\n'))
                print(line.rstrip('\n'))
                return res

    else:
        print(f"Файл {filename} не найден")

print(search_file('fact.py'))