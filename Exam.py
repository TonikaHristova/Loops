number = int(input())
count_p1 = 0
count_p2 = 0
count_p3 = 0
count_p4 = 0
count_p5 = 0

for i in range(0,number):
    input_number = int(input())
    if input_number < 200:
        count_p1 += 1
    elif input_number >= 200 and input_number <=399:
        count_p2 += 1
    elif input_number >= 400 and input_number <= 599:
        count_p3 += 1
    elif input_number >= 600 and input_number <= 799:
        count_p4 += 1
    elif input_number >= 800:
        count_p5 += 1


print("% 0.2f"%(count_p1 / number *100) + "%")
print("% 0.2f"%(count_p2 / number *100) + "%")
print("% 0.2f"%(count_p3 / number *100)+ "%")
print("% 0.2f"%(count_p4 / number *100)+ "%")
print("% 0.2f"%(count_p5 / number *100)+ "%")