
























import math
import sys
name=input("enter your name :")
if name.isalpha():
    age=input("enter your age:")
    if age.isalpha():
        print("invalid input age can only be integer")
    else:
        for i in range(1000):
            print("\n)
            print("enter your choice")
            choice=int(input("....."))
            if choice==1:
                num1=input("enter first any number")
                num2=input("enter second number")
                if (num1.isalpha()or num2.isalpha())










#deepa phuyal,namita ghimere,seema dhungana.






#ask user to enter 10 numbers using input statement and add them to the list.
number = input("enter multiple values: ").split()
x=number


print("number of list is: ",x)

print ("hello"+"world")
#print("hello"+"world")  #concatenation
'''
num=0
name='sant'
marks=9.8
#print(type(name))  type function chechs the data type of the variable

print("My name is "+name)
print("the value of num is ",num)
print("the value is "+str(num))   #this is type casting

print("my namme is %s and my marks are %.2f" %(name,marks))    # plaaceholders


num1= input('enter a number')
num2=int(input('ener second number'))
#by default return type of input function is string
print(int(num1)+num2)
if int(num1)>num2:
    print("result is ready")
    print('num1 is greateer')
else:
    print('num2 is greater')

 '''

#Logical operator and , or ,not


marks=int(input('enter your marks'))
if marks>90 and marks<100:
    print("A")
elif marks >80 and marks<90:
    print("B")

