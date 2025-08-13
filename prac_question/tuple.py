             # Create a Tuple of Cities  -  Scenario: You want to store a list of Indian metro cities.

cities=("mumbai","delhi","kolkata","chennai")
print(type(cities))

            #  Access a Tuple Element - Scenario: You want to access the 2nd city from the tuple.
print(cities[1])

            # Tuple Length
print(f"tuple lenght: {len(cities)}")

            # Check Existence of an Element

if "bangalore" in cities:
    print("yess")
else:
    print("nopee")

            # You want to print all items in a read-only configuration.
for i in cities:
    print(f"city name : {i}")

                # How do you convert a list to a tuple?

l=["hello","how","why"]
k=(tuple(l))
print(k)
print(type(k))

                #Tuple Unpacking - Scenario: You store student details (name, age, city) in a tuple.

student_details=("varnika","10","Meerut")
(name, age, city)=student_details
print( "name:" ,name)
print("age:",age)
print("city:" ,city)

  # You store employee records as ('John', (101, 'HR')). - How do you access the department name 'HR'?

employee_details=('John', (101, 'HR'))
a=employee_details[1]
print(a)
department=a[1]
print(f"department: {department}")

            # How can you concatenate two tuples?

tup1=("bhumi","naina","shivi")
tup2=("meerut","agra","lucknow")
tup3=tup1+tup2
print(tup3)

    # Count a Value in Tuple - Scenario: You want to count how many times a product appears in the inventory.
num=(1,2,4,3,5,2,3,4,5,6)
for i in num:
    a=num.count(i)
    print(f"{i} : {a}")

     # Scenario: You want to get the last value of a tuple. - How do you use negative indexing with a tuple?

print( "last value in tuple is: " ,num[-1])

# You accidentally created t = (5) which behaves like an int. How do you correctly define a single-element tuple?

t=(5,)
print(type(t))

# You need to update a tuple's value indirectly. How do you convert a tuple to a list, change a value, and convert it back?

tu=(1,2,3,4,"hii",9)
y=list(tu)
y.insert(4,10)
y.remove("hii")
x=tuple(y)
print(x)

# You have two lists: names and scores. How do you use zip() to create a list of tuples?

name=("bhumi","naina","shivi")
scores=(90,79,89)
r=zip(name,scores)
print(list(r))
print(type(r))

           # You want to ensure all settings in a tuple are the same value. How do you check if all items in a tuple are equal?
same=(5,5,5,5,5,5)
for i in same:
    for y in range(len(same)):
        if i==same[y]:
            print("all items are same: ")
            break
    # print("all items are same")
        else:
            print("all items are not same ")

# You want to know which day had the lowest and highest temperature. How do you get the index of the min/max element in a tuple?

temps = (30, 25, 27, 32, 28)
min_temp=temps.index(min(temps))
max_temp=temps.index(max(temps))
print("index of lowest temperature: "  ,min_temp)
print("index of highest temperatur: ",max_temp)

# You want to create a tuple of squares.Why can’t we use list comprehension directly to create a tuple and what’s the workaround?

sq=tuple(x**2 for x in range(5))
print(sq)





