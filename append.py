# l=[]
# for i in range(1,6):
#     a=input("enter list item: ")
#     l.append(a)
# print(l)
# for i in range(len(l)):
#     if l[i]=="palak":
#         print(i)
# subject=["math","english","hindi","physics","chem"]
# marks=[23,45,67,89,23] 

# for i in l:
#     for x in subject:
#         for y in marks:
#             print(f"{}")

name=['riya','geeta','palak']
marks=[[23,45,56,67,78],[53,39,67,56,89],[93,68,45,75,25]]
for i in marks[0]:
        print(f"{name[0]} : {i}")

for i in marks[1]:
        print(f"{name[1]} : {i}")

for i in marks[2]:
        print(f"{name[2]} : {i}")

 # print(f"{marks[i][j]}")
        # for j in range(len(marks[i])):
        #     print(f"{marks[i][j]}")


names=["himanshu","vivek","prabhat"]
marks=[
    [30,49,50,70,20],
    [60,40,30,46,65],
    [59,90,30,20,60]
]
for i in range(len(names)):
    for mark in marks[i]:
        print(names[i] + str(mark))
        
     






       

