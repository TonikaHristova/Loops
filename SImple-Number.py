import math

num = int(input())
is_prime = True

if num < 2:
    print("Not prime")
for i in range(2, int(math.sqrt(num)+1)):
    if num / i == 0:
        is_prime = False

print(is_prime)







