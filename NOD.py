a = int(input())
b = int(input())


if a > b:
    while b !=0:
        oldB= b
        b = a % b
        a = oldB
    print(a)
elif a == b:
    print(a)
elif a < b:
    while a!=0:
        oldA = a
        a = b % a
        b = oldA
    print(b)


