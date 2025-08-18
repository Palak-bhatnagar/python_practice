n=int(input("enter any INT value: "))
i=0
# while i<11:
#     a=(f"{n}x{i}={n*i}")
#     print(a) 
#     if i==5 :
#         break
#     i += 1




n=int(input("enter any INT value: "))
main_list=[]
sub_list=[]
k=1
y=1
while k<n:
    sub_list.clear()
    while y<=3:
        a=int(input("enter any number: "))
        sub_list.append(a)
        y+=1
    main_list.append(sub_list)
    k+=1
print(main_list)




# n = int(input("Enter how many sublists you want: "))
# main_list = []

# k = 1
# while k <= n:
#     sub_list = []
#     y = 1
#     while y <= 3:
#         a = int(input(f"Enter number {y} for sublist {k}: "))
#         sub_list.append(a)
#         y += 1
#     main_list.append(sub_list)
#     k += 1

# print(main_list)






# while i<10:
#     a=int(input("enter 10 numbers: "))
#     main_list.append(a)
#     i+=1
# print(main_list)

# p=0
# while p<len(main_list):
#     index=main_list[p]
#     if index%2==0:
#         sub_list.append(index)
#     p+=1
# print(sub_list)
    



   