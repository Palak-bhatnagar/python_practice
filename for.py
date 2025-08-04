# n=int(input("enter any number: "))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")

l=["palak","varun","bhumi","sneha","akshara"]
for x in range(len(l)):
    print(f"{l[x]}=={x}")
for x in "bhumi":
    print(x)
    
for x in l:
    print(x)
    if x=="sneha":
        break
print("end loop")

