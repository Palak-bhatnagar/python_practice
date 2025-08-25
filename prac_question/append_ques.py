#            # Create a list of fruits: ["apple", "banana"]. Append "mango" to the list and print the final list.
# fruits= ["apple", "banana"]
# fruits.append("mango")
# print(fruits)

#             # Ask the user to enter 3 favorite colors one by one. Append each to a list and display the list
# # colours=[]
# # for i in range(3):
# #     color=input("enter your favorite colour: ")
# #     colours.append(color)
# # print(colours)

#     #       Create an empty list. Append the square of numbers from 1 to 5 into it using a loop. Print the list.

# square=[]
# for i in range(6):
#     s=i*i
#     square.append(s)
# print(square)

#             # From the range 1 to 20, append only numbers divisible by 3 into a list. Print the final list.
# for i in range(20):
#     if i %3==0:
#         print(i)

#             # Given:list1 = [1, 2] , list2 = [3, 4] Use append() to add list2 to list1. Print list1. What will be the length of list1?
# list1 = [1, 2] 
# list2 = [3, 4]
# list1.append(list2)
# print(list1)
# print("length of list1: ",len(list1))

#         # Write a program that takes 2 user inputs: name and age. Append them as a dictionary to a list. Repeat for 3 users.

# # student=[]
# # for i in range(3):
# #     name=input("enter name: ")
# #     age=input("enter age: ")
# #     details={
# #         "name":name,
# #         "age":age
# #     }
# #     student.append(details)
# # print(student)    

#         # Create a list: students = [["Alice", 85], ["Bob", 90]]. Append a new student ["Charlie", 88] using append().

# students = [["Alice", 85], ["Bob", 90]]
# new=["Charlie", 88]
# students.append(new)
# print(students)

# # Python List Append Practice Questions Use nested loops to create a 3x3 matrix:[[0, 1, 2], [0, 1, 2], [0, 1, 2]]. Use only append() to build it.
# matrix1=[]
# for i in range(3):
#     sub_list=[]
#     for a in range(3):
#         b=input("enter any num: ")
#         sub_list.append(b)
#     matrix1.append(sub_list)
    
# print(matrix1)

           # Given: scores = [45, 67, 23, 90, 88]. Append only scores > 50 to a new list called passed.
scores = [45, 67, 23, 90, 88]
new=[]
for item in scores:
    if item>50:
        new.append(item)
print(new)

           # Take 5 numbers as input from the user, append them to a list. Sort the list and print it.

num_list=[]
for i in range(5):
    a=input(f"enter {i} num: ")
    num_list.append(i)
print(num_list)







