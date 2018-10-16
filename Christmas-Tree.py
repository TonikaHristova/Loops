num = int(input())


print((num+1)* " " + "|")

for row in range(1, num+1):
   print(" " * (num - row) + "*" * row + " " + "|" + " " + "*" * row)



