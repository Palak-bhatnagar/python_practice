                        # Create a dictionary to store the names of 5 students as keys and their marks as values. Print all keys and values

names={
    "shivi":90,
    "palak":58,
    "bhumi":89,
}

for i in names.items():
    print(i)

                                # Write a Python program to access the value of a specific key in a dictionary.

print(names.get("bhumi"))

                                # . How do you add a new key-value pair to a dictionary? Give an example
        
names.update({"alia" : 76})
names["anshi"]=67
print(names)

                                # Write a program to remove a key from a dictionary using pop().


# names.pop("alia")
# print(names)


                                # Write a program to check if a given key exists in a dictionary
# i=input("Enter the key: ")
# for key in names.keys():
#     found=False
#     if i in names:
#         found=True
#         break
#     else:
#         found=False
# print(found)
                                      

                                    #   Create a dictionary and print only the keys using a loop.

for key in names:
    print(key)                                    

                         # Write a program to count the frequency of each character in a string using a dictionary

                         