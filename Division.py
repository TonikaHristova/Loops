number = int(input())
count_1 = 0
count_2 = 0
count_3 = 0

for i in range(0, number):
    input_number = int(input())
    if input_number % 2 == 0:
        count_1 += 1

    if input_number %3 == 0:
        count_2 += 1

    if input_number % 4 == 0:
        count_3 += 1


print("%0.2f" % (count_1 / number * 100) + "%")
print("%0.2f" % (count_2 / number * 100) + "%")
print("%0.2f" % (count_3 / number * 100) + "%")