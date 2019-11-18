'''def calc(a,b):
    sum = a+b
    sub = a-b
    return sum,sub
a=int(input("enter one number"))
b=int(input("enter second number"))

sum,sub=calc(a,b)
print("the sum is",sum)
print("sub is",sub)'''

# return the function
'''
def aoc(r):
      a=3.14*r*r
      return a
r= int(input("enter the radius of a circle"))
aoc=aoc(r)
print("area of circle is",aoc)

'''
#power of a number
'''
def pow(a,b):
    n=a**b
    return n
a=int(input("enter the base number"))
b=int(input("enter the power number"))
v=pow(a,b)
print(v)
'''

'''
#amstrong number
def ams():
    n = int(input("enter any three digit number"))
    m=n
    s=0
    while n>0:
        a=n % 10
        s=s+a**3
        n=n//10

    if s==m:
        print("it is amstrong number")
    else:
        print("it is not number")
ams()
'''
'''
#factorial
def fac():
    f=1
    n = int(input("enter the number"))
    for i in range(1,n+1):
        f=f*i
    return f

v=fac()
print(v)
'''

'''
#palindrome
def palindrome():
    n=int(input("enter the nnumber"))
    m=n
    s=0
    while n>0:
        r=n%10
        s=s*10+r
        n=n//10
        
    if m==s:
        print("it is palindrome")
    else:
        print("it is not a palindrome")
v=palindrome()


'''








#for loop in which we soecify the range of vaues and how many times we want to execute
#for x in range(2,100,2):
 #   print(x)
#i=0
#while i<10:
 #    print(i)
  #   i+=1   # i=i+1  #i++

#name=input('Enter name ')
#while name.isalpha()==False or len(name)<3:
 #   print("WRONG INPUT")
  #  name = input('Please Enter correct name ')
#print(len(name))
#print("welcome",name)
'''

print (True and True)
print (True and False)
print (False and False)    # and ---->  multiplicationn True-1 False -0
print (False and True)




print (True or True)
print (True or False)# or ---->  addition  True-1 False -0
print (False or False)
print (False or True)


'''