# n=int(input("enter any number: "))
# for i in range(1,11):
#     print(f"{n}X{i}={n*i}")

# l=["palak","varun","bhumi","sneha","akshara"]
# for x in range(len(l)):
#     print(f"{l[x]}=={x}")
# for x in "bhumi":
#     print(x)
    
# for x in l:
#     print(x)
#     if x=="sneha":
#         break
# print("end loop")



# print even number from 1-20

# for i in range(20):
#     if i %2==0:
#         print(i)
    



# sum=0

# for i in range(100):
#     sum+=i
# print(sum)




# . Print the multiplication table of 5 using a for loop.

# for i in range(11):
#     print(f"5X{i}= {5*i}")


#   5. Print each character of a string using a for loop
# name= "palak"
# for i in name:
#     print(i)

               # Reverse a string using a for loop

# a=len(name)-1
# revrse=""
# for i in name:
#     revrse= i+revrse
# print(revrse)
    
          # 7. Count the number of vowels in a string using a for loop.

# chracter=input("enter any word: ")
# sentence=chracter.lower()
# vowel=['a','e','i','o','u']
# sum=0
# for i in sentence:
#     if i in vowel:
#         sum+=1
# print(sum)
                            # . Find the largest number in a list using a for loop.

# l=[23,45,8,7,98,56,87,3,7]
# maxnum=l[0]
# for item in l:
#     if item>maxnum:
#         maxnum=item
# print(maxnum)


                        # Print all elements of a 2D list using nested for loops.

# list=[[1,2,3],[5,6,7]]
# for i in list:
#     for j in i:
#         print(j)



                        # . Check if a number is prime using a for loop

# n=int(input("enter any number: "))
# for i in range(2,n):
#     if n%i==0:
#         print("no. is not prime :",n)
#         break
# else:
#     print("no. is prime:" ,n)
    
                        
                    #    Generate a Fibonacci sequence of n terms using a for loop
# 0,1,1,2,3,5,8,13
# n=int(input("enter any number: "))
# a=0
# b=1
# print(a,b, end=" ")
# i=1   
# for i in range(n):
#     fab=a+b
#     a,b=b,fab
#     print(fab , end=" ")
    



 #   Remove duplicates from a list using a for loop (without using set).

# thislist=[23,6,90,78,53,23, 3,8,6,3]
# newlist=[]
# for i in thislist:
#     if i not in newlist:
#         newlist.append(i)
# print(newlist)

 # Count frequency of each element in a list using nested for loops.
 
# countlist=[1,2,3,2,4,5,4,3,2,7,8,9]
# newlist=[]
# for i in range(len(countlist)):
#     if countlist[i] not in newlist:
#         count=0
#         for k in range(len(countlist)):
#             if countlist[i]==countlist[k]:
#                 count+=1
#         newlist.append(countlist[i])
#         print(f"{countlist[i]}: {count}")
            


    # for x in countlist:
    #     if x == i:
    #         count+=1
    # print(x,":" ,count)
      
        













           # Flatten a nested list (one level) using a for loop.
# thislist=[[23,6,90],[78,53,23],[3,8,6,3]]
# newlist=[]
# for i in thislist:
#     for y in i:
#         newlist.append(y)
# print(newlist)    




        #  5. Loop over a dictionary and print key-value pairs using a for loop.


# thisdict =	{
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }

# for i in thisdict:
#     print(i,":" ,thisdict[i])


      # Count frequency of each element in a list using nested for loops.

# thislist=[1,2,3,4,1,2,3,6,7,5,7,8,9,7,8]
# newlist=[]
# for i in range(len(thislist)):
#     if thislist[i] not in newlist:
#         count=0
#         for k in range(len(thislist)):
#             if thislist[i]==thislist[k]:
#                 count+=1
#         newlist.append(thislist[i])
#         print(f"{thislist[i]} : {count}")



thislist=[1,2,3,4,2,3,4,5,7,5,4,8,6]
newlist=[]
for i in range(len(thislist)):
    if thislist[i] not in newlist:
        count=0
        for k in range(len(thislist)):
            if thislist[i]==thislist[k]:
                count+=1
        newlist.append(thislist[i])
        print(f"{thislist[i]}: {count}")
                



