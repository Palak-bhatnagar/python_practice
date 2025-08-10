def sum_num(a,b):
    return a+b
# num1=int(input("enter 1st num : "))
# num2=int(input("enter 2st num : "))
# print(sum_num(num1,num2))




def calculator(o,x,y):
    if o=='+':
        print(x+y)
    elif o=='-':
        print(x-y)
    elif o=='*':
        print(x*y)
    else:
        print("invalid operator")
    
operator=input("enter any operator like +,-,* : ")
num1=int(input("enter 1st num : "))
num2=int(input("enter 2st num : "))
calculator(operator,num1,num2)
    
