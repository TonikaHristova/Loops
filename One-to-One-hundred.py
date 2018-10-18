number = int(input("Enter a number in the range [1...100]: "))

while number<1 or number>100:
     print("Incorrect number!")
     print(("Enter a number in the range [1...100]: "))
     number = int(input())
if number >=1 and number <=100:
         print("The number is: " + str(number))









