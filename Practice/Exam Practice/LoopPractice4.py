result = []
for n in range(100,1001):
    if n % 5 == 0 and n % 6 == 0:
        result.append(n)
print(result)
