l=[12,3,5,7,8,10,9,35,67,12]
even=0
odd=0
for i in l:
    if i%2==0:
        even+=i
    else:
        odd +=i
print(f"sum of even number is: {even}")
print(f"sum of odd number is: {odd}")

marks=[51,52,54,55,45,]
sum=0
for i in marks:
    sum+=i
percentage=sum/5
print("your percentage is :",percentage)

if percentage>75:
    print("pass with distinction")
elif percentage>=60 and percentage<75:
    print("pass with 1st division")
elif percentage>=33 and percentage<60:
    print("printpass with second division")
else:
    print("you are fail. try nnext time")
