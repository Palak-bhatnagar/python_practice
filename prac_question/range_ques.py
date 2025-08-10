# Print numbers from 0 to 9 using range.


# for i in range(10):
#     print(i)

# for i in range(2,11):
#     if i%2==0:
#         print(i , end=" ",)


# Create a list from 0 to 5 using range and list() function.
# num=[]
# for i in range(0,6):
#     num.append(i)
# print(num)



# What will range(5, 15, 2) produce? Write a program to print it.

# for i in range(5,15,2):
#     print(i)



        # Use range to print numbers in reverse from 10 to 1

# for i in range(10,0,-1):
#     print(i)


# Print all multiples of 3 between 1 and 30 using range

# for i in range(1,31):
#     if i %3==0:
#         print(i, end=" ")


         # What is the output of list(range(10, 0, -2))? Explain.

for i in range(10,0,-2):
    print(i, end=" ")
print()
for i in range(10,0,-1):
    print(i)

        #Use a for loop and range to calculate the sum of numbers from 1 to 100.

# sum=0
# for i in range(1,100+1):
#     sum=sum+i
# print(sum)


# Check if a number exists in a given range or not (e.g., is 15 in range(10, 21)?)

# for i in range(10,21):
#     if i==15:
#         print(True)
#     else:
#         print(False)
#         break

# Generate a list of squares of all odd numbers between 1 and 20 using list comprehension and range.

# sqr=[]
# for i in range(1,20):
#     if i%2!=0:
#         print(i ,":", i**2)

# Using range, write a function to return the nth Fibonacci number using iteration (no recursion)
# m=int(input("enter no. "))
# a=0
# b=1
# print(a,b ,end=" ")

# for i in range(m):
#     fab=a+b
#     a,b=b,fab
#     print(fab,end=" ")


# Create a program to print a pattern using nested range loops: * ** *** ****

for i in range(1,5):
    print("*"*i, end=" ")

