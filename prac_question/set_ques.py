#  How do you create an empty set in Python? Why is {} not used for this purpose?

s=set()
                   
                   # Write a Python program to create a set with elements 1, 2, 3, 4, 5

s.add(1)
s.add(2)
s.add(3)
s.add(4)
print(s)

                # How can you check if a specific element exists in a set?
num={2,3,4,5,6,7,1}
# if 5 in s :
#     is_exist=True
# else:
#     is_exist=False
# print(is_exist)

for i in num:
    if i==3:
        is_exist=True
        break
    else:
        is_exist=False
print(is_exist)

                # What happens if you try to access a set element by index (e.g., myset[0])? Explain why.

                # . Write a program to iterate through all elements of a set using a for loop.
for i in s:
    print(i)

                #  Create a set containing the numbers 10, 20, 30, then add the number 40 to it.

numbers={10,20,30}
numbers.add(40)
print(numbers)

                # How do you add multiple elements {50, 60, 70} to an existing set?

a={50,60,70}
numbers.update(a)


                # . Write a program to remove an element 30 from a set using remove(). What happens if the element is not found?

numbers.remove(30)
print(numbers)

                        # Write a program to remove an element 30 from a set using discard(). What happens if the element is not found?

numbers.discard(10)
print(numbers)


                        # How do you remove and return a random element from a set? Write an example.

a=numbers.pop()
print(a)
print(numbers)

#                     # . Write a program to clear all elements from a set without deleting the set itself.
# print(num)                    
# num.clear()
# print(num)

# How do you find the union of two sets {1, 2, 3} and {3, 4, 5}?

set1={1, 2, 3}
set2={3, 4, 5}
set3=set1.union(set2)
print(set3)

# How do you find the intersection of two sets {1, 2, 3} and {2, 3, 4}?
set4=set1.intersection(set2)
print(set4)

# Write a program to get elements present in set A but not in set B (Difference).

a={"a","b","c"}
b={"a","g","d"}
c=a.difference(b)
print(c)

# Write a program to get elements that are in either set A or set B but not in both (Symmetric Difference).

d=a.symmetric_difference(b)
print(d)

    # How do you check if one set is a subset of another? Give an example.

sett={2,1,3,4,5,6}
sub_set={1,4,5}
f=sub_set.issubset(sett)
print(f)

            # . How do you check if two sets are disjoint? Give an example

g=sett.isdisjoint(sub_set)
print((g))

