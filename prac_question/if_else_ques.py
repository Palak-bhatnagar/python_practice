# l=[12,3,5,7,8,10,9,35,67,12]
# even=0
# odd=0
# for i in l:
#     if i%2==0:
#         even+=i
#     else:
#         odd +=i
# print(f"sum of even number is: {even}")
# print(f"sum of odd number is: {odd}")

# marks=[51,52,54,55,45,]
# sum=0
# for i in marks:
#     sum+=i
# percentage=sum/5
# print("your percentage is :",percentage)

# if percentage>75:
#     print("pass with distinction")
# elif percentage>=60 and percentage<75:
#     print("pass with 1st division")
# elif percentage>=33 and percentage<60:
#     print("printpass with second division")
# else:
#     print("you are fail. try nnext time")


#                                             1. Write a program to check if a number is positive or negative.


# num=int(input("enter every number: "))
# if num>0:
#     print("number is positive")
# else:
#     print("number is negative: ")

         #  Write a program to input a person's age and print 'Minor' if less than 18, 'Adult' if between 18 and 60, and 'Senior' if 60 or above.
# if num>0 and num<18:
#     print("MINOR!!!")
# elif num>18 and num<60:
#     print("ADULT!!!")
# elif num>60:
#     print("SENIOR!!!")
# else:
#     print("INVALID AGE: ")

                # write a program that checks if a character entered is a vowel or a consonant.

chracter=input("enter any char: ")
vowel='eaiou'

if chracter in vowel:
    print("vowel")
else:
    print("consonant") 

# if 'a' in "apple":
#     print("yes")
       

     # 6. Write a Python program to input marks of a student and print the grade: - 90-100 → A - 80-89 →B - 70-79 → C - 60-69 → D - <60 → F

# num=int(input("enter every number: "))
# if num>90 and num<100:
#     print("GRADE: A")
# elif num>80 and num>89:
#     print("GRADE: B")
# elif num>70 and num<79:
#     print("GRADE: C")
# elif num>60 and num<69:
#     print("GRADE: D")
# elif num<60:
#     print("GRADE: F")

# Write a calculator program that takes two numbers and an operator (+, -, *, /) from the user and performs the operation using if-elif-else.


# num1=int(input("enter every number: "))
# num2=int(input("enter 2nd number: "))
# operator=input("operator like + - * / : ")
# if operator == '+':
#     a=num1+num2
#     print(a)
# elif operator == '-':
#     b=num1-num2
#     print(b)
# elif operator == '*':
#     c=num1*num2
#     print(c)
# elif operator == '/':
#     d=num1/num2
#     print(d)



# Write a Python program that simulates a simple login system with a stored username and password. Use if-else to check credentials.

# stored_username="palak bhatnagar"
# stored_pass="12345"

# username=input("enter username: ")
# passwd=input("enter password: ")
# if stored_username==username and stored_pass==passwd:
#     print("your credentails are correct ")
# else:
    # print("Invalid")


        #            leap year find
# num1=int(input("enter any year: "))
# if num1%400==0 and num1%100==0:
#     print(num1 ,"is leap year")
# elif num1%4==0 and num1%100!=0:
#     print(num1 ,"is leap year")
# else:
#     print(num1, "is not leap year")












