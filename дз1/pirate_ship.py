n, m = map(int, input().split())

goods = []
for _ in range(m):
    parts = input().split()
    name = parts[0]
    weight = int(parts[1])
    value = int(parts[2])
    goods.append((name, weight, value))

goods.sort(key=lambda x: x[2] / x[1], reverse=True)

capacity = n
output_lines = []

for name, weight, value in goods:
    if capacity <= 0:
        break
    take = min(weight, capacity)
    taken_value = value * (take / weight)
    output_lines.append((name, take, taken_value))
    capacity -= take

for name, w, v in output_lines:
    print(f"{name} {w:.2f} {v:.2f}")