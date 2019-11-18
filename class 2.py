'''
arr=[1,2.9,'sant']   #list values can store any kind of values
tuples=(1,2.9,'sannt')  #tuples
print(arr)
print(tuples)
print(arr[2])
print(tuples[0])   #indexing

new_list=[1,2,3,4,55,6,7,8,0]
print(new_list[2:6]) #slicing start:end-1:step

nlist=[1,2,3,4,5,6,7,8,9,10,11,12]
print(nlist[1:12:2]) #specifying the value for step'''
'''

#append,pop,count,extend,sum

list1=[1,2,3,4,4,5,2,3,6,7]
list1.append(8) #adds a value to the end of list
print(list1)


list1.pop(1)
print(list1)  #removes a value based on the index

print(list1.count(2))


list2=['a','b','c']
list2.extend(list1)
print(list2)  #it extends a list with other list

print(sum(list1))
tuple=('1',2,3)
tuple.append(2)'''

list1=[4,2,10,12,1,14,6]
list2=['x','a','w','c']
name='saabbbccdddddeeee'
print(name[2])
print(name[1:3])
print(name.count('b'))
list1.sort(reverse=True) #by defult --> ascending and reverse=True --> desc
list2.sort()
print(list1)
print(list2)
name.append("b")
print(name)
