                               # 2. Write a Python program to remove the number 3 from this list: numbers = [1, 2, 3, 4, 5]
# numbers=[1,2,3,4,5]
# numbers.remove(3)
# print(numbers)

                                # 6. How would you remove all occurrences of the value 5 from the list: nums = [5, 1,2, 5, 3, 5, 4]?

# nums = [5, 1,2, 5, 3, 5, 4]
# nums.remove(5)
# nums.remove(5)
# nums.remove(5)
# print(nums)

                                #  Given a list of strings, remove the string 'apple' only if it exists. fruits = ['banana','orange', 'apple', 'mango']

# fruits = ['banana','orange', 'apple', 'mango']
# if 'apple' in fruits:
#     fruits.remove("apple")
# print(fruits)


                                   # Write a function that removes all duplicate elements from a list without using set().
list1=[1,3,2,4,5,4,2]
def dup_remove(x):
        new=[]
        for ele in list1:
                if ele not in new:
                        new.append(ele)
        print(new)              
    
dup_remove(list1)

                    # Given a list of dictionaries, remove all dictionaries where 'status' is 'inactive'.    








                   # Write a program to remove all negative numbers from a list using a loop and remove().

neg=[2,1,-3,4,-5,5,2,-4,6,8,-9]
for i in neg:
        if i <0:
                neg.remove(i)
print(neg)


