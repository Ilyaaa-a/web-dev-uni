adult_sum = 0.0
pensioner_sum = 0.0
child_sum = 0.0

with open('products.csv', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for line in lines[1:]:
    parts = line.strip().split(',')

    adult_sum += float(parts[1])
    pensioner_sum += float(parts[2])
    child_sum += float(parts[3])

print(f"{adult_sum:.2f} {pensioner_sum:.2f} {child_sum:.2f}")