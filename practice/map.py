# fruits=["apple", "mango", "cherry"]
# sub_list=[fruit.upper() for fruit in fruits ]
# print(sub_list)
# for i in fruit:
#     print(i.upper())


# names = ["Alice", "Bob", "Charlie"]
# ages = [25, 30, 35]

# combined = zip(names, ages)
# print(list(combined))
# print(type(combined))

# num=[2,3,4,5,6,7]
# square=map(pow ,num,[2]*len(num))
# print(list(square))


num=int(input("how many students are in the class: "))
name_list=[]
mark_list=[]
sub_list=[]
for i in range(num):
    name=input("enter name: ")
    name_list.append(name)
    for y in range(0,5):
        marks=input("enter your marks: ")
        sub_list.append(marks)
        
    mark_list.append(list(sub_list))
    sub_list.clear()

print(name_list)
print(mark_list)