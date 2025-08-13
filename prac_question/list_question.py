# # Q1. Store Names of Students: You want to store the names of 5 students in a class. How will you create and print a list of student names?
# name=["rohan","mohan","seema","diya","jiya"]
# for i in range(5):
#     print(name[i])

# # Q2. Accessing Elements: You want to greet the first student in the list. How do you access the first element in a list?

# print(f"hello, {name[0]}")


# # Q3. Updating List Items: A student changed their name. How do you update the second item in the list?
# name.pop(1) #name.remove("mohan")
# name.insert(1,"amit")
# print(name)


# # Q4. Append New Student: A new student joins the class. How do you add this new student to the end of the list?

# name.insert(len(name), "shivi")
# print(name)
# # Q5. Remove a Student Who Left: A student has left the class. How do you remove the student named "Amit" from the list?
# name.remove("amit")
# print(name)


# # Q6. List of Marks: Average Calculation: You have marks of a student: [85, 90, 78, 92].Write code to calculate the average mark using the list.

# student= [85, 90, 78, 92]
# sum=0
# for i in student:
#     sum+= i
# print("sum: ",sum)

# a=sum/(len(student))
# print("average is: ",a)


# Q7. Sort Students by Marks: You have student marks: [45, 78, 67, 89, 90]. How do you sort the marks in descending order?

# marks= [45, 78, 67, 89, 90]
# marks.sort(reverse=True)
# print("marks in descending order:", marks)

       # Q8. Find Duplicates in a List: Some students registered multiple times. How do you find and print duplicate names in a list?

stu=["rohan", "kirti","mohan","seema","kirti","diya","mohan","jiya","seema","shruti","rohan"]
new=[]
duplicate=[]
for i in stu:
    if i not in new:
        new.append(i)
    else:
        # duplicate.append(stu)
        print(f"duplicate names : {i}")
        



              # Q9. Combine Two Lists: You have two batches of students. How do you merge two lists of student names?

# name2=["riya","naina","varnika","dishi"]
# name.extend(name2)
# print("extended list is: ",name)

# Q10. List Comprehension - Square of Marks: You want to store square of marks for further calculations. Use list comprehension to generate squares from [10, 20, 30].

# list1=[ x**2 for x in range(0,100,10)]
# print(list1)

# Q11. Remove All Duplicates Without Using Set: Maintain original order while removing duplicates.
# Write a program to remove duplicates from a list without using set().

# names3=["rohan","mohan","seema","diya","mohan","jiya","seema","shruti","rohan"]
# newlis=[]
# for i in range(len(names3)):
#     if names3[i] not in newlis:
#         newlis.append(names3[i])
# # names3.clear()
# names3=newlis      
# print(names3)   


# Q12. Student Marks Above Threshold: From [45, 65, 78, 89, 32], print only marks above 60. How can you filter elements based on a condition?
# m=[45, 65, 78, 89, 32]
# a=tuple(filter(lambda n:n>60,m))
# print(f"Marks that are above 60: {a}")


# Q13. Find Most Frequent Element: You want to find the most common name in a registration list. Write code to 
# find the element that appears most frequently in a list.

frequent_num=["bhumi","riya", "shivi" ,"jiya","shivi","teena","shivi","bhumi","shivi"]
new_list=[]
total=0
name=""
for i in frequent_num:
    a=frequent_num.count(i)
    if total>a:
        pass
    else:
        total=a
        name=i

print(f"{name}:{total}")

# Q14. Flatten a Nested List: You have student marks stored like [[90, 80], [75, 85], [60]].Write code to flatten this nested list into a single list.

# num=[[90, 80], [75, 85], [60]]
# empty=[]
# for i in num:
#     print(i)
#     for y in i:
#         empty.append(y)
# print(empty)
    

# Q15. Zipping Two Lists: You have student names and their corresponding marks in two lists. How do you combine them into a list of tuples (name, mark)?

nam=["bhumi","shivi","neha","priya","varnika"]
numbers=[45,47,35,67,89]
names=zip(nam,numbers)
print(list(names))




