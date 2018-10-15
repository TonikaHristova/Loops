num = int(input())

for row in range(num):
    for col in range(num - row - 1):
        print(" ", end="")
    print("*", end="")
