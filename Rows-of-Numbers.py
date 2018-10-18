number = int(input())
result = 1

for i in range(0, number):
    print(result)
    result = result * 2 + 1
    if result > number:

        break
