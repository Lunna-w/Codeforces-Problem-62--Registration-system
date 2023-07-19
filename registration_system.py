t = int(input())

database = {}

for _ in range(t):
    y = input().strip()  
    if y not in database:
        database[y] = 0
        print("OK")
    else:
        database[y] += 1
        print(f"{y}{database[y]}")