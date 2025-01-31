#Print a line asking the user to enter three numbers
#Prompt the user to enter the three integers, one at a time
#Display the three numbers entered, their sum, and the average.
#You can assume the user will only enter positive integers
#Example output: (you do not have to match my words exactly)
#Please enter three whole numbers:
#Number 1: 11
#Number 2: 11
#Number 3: 12
#The sum of 11 and 11 and 12 is 34 and the average is 11.333333333333334.

print('please enter 3 whole numbers')
number = any
Number1 = int(input(number ))
Number2 = int(input(number ))
Number3 = int(input(number ))
Sum = Number1 + Number2 + Number3
Average = Sum / 3
answer= f"The sum of {Number1} and {Number2} and {Number3} is {Sum} and the average is {Average}."
print(answer)