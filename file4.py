#-----> while loop
#-----> berak usimg while loop

'''
# eg:1
# iterate from 20 to 30 and break the loop in 27
# i = 20
# while i<31:
#    print(i)
#    i+=1

#    if i==27:
#        break

# 2.)
# i = 20
# while i<31:
#    print(i)
    
#    if i == 27:
#       break
#    i+=


# i = 20
# while i<31:
#    i=i+1
#    if i==27:
#          continue
#    print(i)

# ! Eg:5
# while to iterate from 12 to 22
# find the sum of all numbers

# i = 12
# while i<22+1:
#     print(i)
#    i+=1

# i = 12
# sum=0
# while i<23:
#   sum=sum+i
#   i+=1
# print(sum)

# ! Eg:6
# find the average of value from 20 to 25

# i=20
# sum=0
# while i<=25:
#    sum=sum+i
#    avg=sum/6
#   i+=1
# print(avg)

# i=20
# sum=0
# count = 0
# while i<=25:
#    sum = sum+i
#   count+=1
#   i+=1
# print(sum/count)


for row in range(1, 3+1):
    for col in range(1, 4+1):
        print(row, col)


for row in range(8):
    for col in range(8):
        print("*",end=" ")
    print()
for row in range(8):
    for col in range(8):
        print("*",end=" ")
    print()


#! to print stsrs in right angled triangle


for row in range(0, 6):
    for col in range(0, row):
        print("*", end=" ")
    print()


#Eg:3
# * * * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
 
rows = 6

for i in range(rows, 0, -1):
    for j in range(0, i):
        print("*", end=' ')
    print("\n")


#*****
#*   *
#*   *
#*   *
#*****

rows = 5
cols = 5

for i in range(rows):
    for j in range(cols):
        if i == 0 or i == rows - 1 or j == 0 or j == cols - 1:
            print("*", end='')
        else:
            print(" ", end='')
    print()


for row in range(5):
    for col in range(5):
        if col==0 or col==5-1 or row ==0 or row ==5-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


#      *
#    * * *
#   * * * *
#  * * * * *

rows = 9

for i in range(rows):
    print(" " * (rows - i - 1), end='')  
    print("*" * (2 * i + 1), end='')    
    print(" " * (rows - i - 1))



# ! ------> Datatypes
# primary

# number ---> int, float complex
# string
# boolean
# none

# collection
# list
# tuple
# set
# dictionary

# ? -----> List

1.0 if collection of elements are sorounded by square brackets, it is considered
# to be list
# ! eg:1
 11 = [4, 7, 9, 89, "hello' , 7+9j, [8, 9, 0]]

'''
# Characteristics of list
# 1.) List have to be surrounded []
# 2.) It is mutable (the elements in the list are changable)
# 3.) Every elements inside list is indexed
# 4.) The elements inside list will be ordered format
# 5.) It can hold duplicate values
# 6.) Its heterogenous


# to access the elements in list

I1 = [1, 4, 1, 7, 89,7, 7.5, "p", "i"]
print(I1)

# ----> Indexing
# In the collection datatypes like list, tuple, string, the elements will be alloted with predefines unique value called index value

# We have 2 types of indexing
# Positive indexing ---> starts with 0 from left hand side
# Negative indexing ---> starts with -1 from right hand side



# positive indexing
# print(ist1[0])
# print(ist1[4])
#print(ist1[20])--> error

# ? ---> Negative indexing
#lst1 = [1,4,1,7,89,7,5,"p","i"]
#print(lst[-1])
#print(lst[-5])

# ? ---> slicing
lst1 = [1,4,1,7,89,7,5,"p","i"]
#lst[start_index:end_indexstep]

print(lst1[0:4])
print(lst1[6:8])
print(lst1[3:6])
print(lst1[:5])
print(lst1[3:])
print(lst1[:])

#print(lst1[o:7:1]) # lst1[0:7] --->both are same
print(lst1[0:7:2])

# trail = int(input())


lst1 = [1, 4, 1, 7, 89.7, 7.5, "p", "i"]
print(lst1[-4:-1])       
print(lst1[-1:-4]) --> []
print(lst1[-7:-1])
print(lst1[-7:1:2])



        
    




  








