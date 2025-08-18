# Write a Python program that takes an integer input and reverses it using a while loop.
# Write a Python program to count how many digits are in a given number using a while loop.


# # sum of even number 1-10
# l=[3,4,6,2,10,]
# sum=0
# for i in l:
#     if i == 4:
#         continue
#     print(i)

# max = l[0]
# for num in l:
#     if num>max:
#         max=num
# print(max)

# for i in l:
#     if i%2==0:
#         sum += i
    
# print(sum)



# # Input from user
# num = int(input("Enter a number: "))

# # Initialize reversed number to 0
# reversed_num = 0

# # Loop until num becomes 0
# while num > 0:
#     digit = num % 10           # Get the last digit
#     reversed_num = reversed_num * 10 + digit  # Append digit to reversed number
#     num = num // 10            # Remove last digit from num

# # Print the result
# print("Reversed number is:", reversed_num)


# Input from user
num = int(input("Enter a number: "))

# Handle negative numbers
if num < 0:
    num = -num
    is_negative = True
else:
    is_negative = False

# Convert number to string to use for loop
num_str = str(num)

# Create empty string to store reversed digits
reversed_str = ""

# Loop through digits in reverse order
for ch in num_str:
    reversed_str = ch + reversed_str  # Add to front

# Convert back to integer
reversed_num = int(reversed_str)

# Add minus sign if original number was negative
if is_negative:
    reversed_num = -reversed_num

# Print result
print("Reversed number is:", reversed_num)

