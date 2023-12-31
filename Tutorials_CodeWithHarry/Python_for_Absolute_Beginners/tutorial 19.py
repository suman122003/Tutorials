# Tutorial 19 - Exercise 2 - Faulty Calculator Solution
print ('\t Tutorial 19', 'https://youtu.be/s0lxxTHWx6w', '\n')
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Design a calculator which will correctly solve all the problems except the following ones:
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4
# Your program should take operator  and the two numbers as input from the user
# and then return the result
print("Enter 1st Number")
num1 = float(input())
print('Enter 2nd Number')
num2 = float(input())
print('so What you Want?'+'+,-,/,%,*')
num3 =input()
if num1 ==45 and num2==3 and num3=='*':
    print("555")
elif num1 == 56 and num2 == 9 and num3 == '+':
        print("77")
elif num1 == 56 and num2 == 6 and num3 == '/':
        print("4")
elif num3=='*' :
    num4=num1*num2
    print(num4)
elif num3 == '+':
    plus=num1+num2
    print(plus)
elif num3 == '/':
    Dev=num1/num2
    print(Dev)
elif num3 == '-':
    Dev=num1-num2
    print(Dev)
elif num3 == '%':
    percent=num2%num1
    print(percent)
else:
    print("Error! Please check your input")
exit
