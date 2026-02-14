a = input().strip()
b = input().strip()

flag = True
for char in a:
    if a.count(char) != b.count(char):
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
