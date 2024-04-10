#Task 1: Identify the Greatest
#Task 2: Identify the Smallest

number = int(input('Write a 1, 2, or 3: '))
number_2 = int(input('Write another 1, 2, or 3: '))


if number == 3 and number_2 == 1:
    print('The largest number is 3 and smallest number is 1')
elif number == 3 and number_2 == 2:
    print('The largest number is 3 and the smallest is 2')
elif number == 3 and number_2 == 3:
    print('They are both equal')
elif number == 2 and number_2 == 3:
    print('The largest is 3 and the smallest is 2')
elif number == 2 and number_2 == 2:
    print('They are both equal')
elif number == 2 and number_2 == 1:
    print('The largest number is 2 and the smallest is 1')
elif number == 1 and number_2 == 3:
    print('The largest number is 3 and the smallest is 1')
elif number == 1 and number_2 == 2:
    print("The largest number is 2 and the smallest is 1")
elif number == 1 and number_2 == 1:
    print("They are both equal")
else:
    print('"The Greatest among you will be the Least of you"- JC')