                    # Checking if a student's roll number is present in the list of registered participants.

roll_num ={22,14,56,78,98,21,60}
student_roll_num=56
if student_roll_num in roll_num:
    print(f"roll no. {student_roll_num} is a registered participant.")
else:
    print(f"roll num {student_roll_num} is not registered")

                    # Iterate through all elements of a set. Example: Printing all cities where your company has offices.

cities={"meerut","agra","lucknow","jaipur"}
for x in cities:
    print(x)

                    # . Add the number 40 to a set {10, 20, 30}. Example: Adding a new product ID to the store inventory.

s={10, 20, 30}
s.add(40)
print(s)

                    # . Add multiple elements {50, 60, 70} to an existing set. Example: Adding multiple new course IDs to a training institute's database                       

n={50,60,70}
sn=s|n
print(sn)

                                                    # Intermediate Level
        # Remove an element using remove(). Example: Removing a booked seat number from the set when a customer cancels a ticket.

sn.remove(50)
print(sn)

        # Remove an element using discard(). Example: Discarding a student roll number from a class list without error if not found.
roll_num.discard(56)
roll_num.discard(90)
print(roll_num)

                # Remove and return a random element using pop(). Example: Assigning a random unallocated desk to a new employee.
 
randm={3,7,9,"apple","k",10,"33",}
randm.pop()
print(randm)

                # Clear all elements from a set. Example: Clearing all temporary guest passes from a security system
randm.clear()
print(randm)

                # Find the union of two sets. Example: Combining the list of students from Class A and Class B for a sports event.

class_A=["abhi","jiya","shivi","diya"]
class_b={"anu","manu","tiya","dishi"}
combine=class_b.union(class_A)
print(combine)

                # Find the intersection of two sets. Example: Finding customers who are subscribed to both email and SMS notifications.

email={"abhi","jiya","shivi","diya","anu"}
sms={"anu","manu","diya","dishi"}
email.intersection_update(sms)            #(apply only b/w sets)
print(email)

                                    # Difference of sets. Example: Finding items in the warehouse that are not listed in the online store.

warehouse={"tv","micro-wave","fridge","mixer","mobile","laptop","desktop"}
online_store={"micro-wave","fridge","mixer","mobile","desktop"}
items=warehouse.difference(online_store)
print(items)

                                  # Symmetric difference. Example: Finding skills that are in either Job Applicant A or Applicant B but not in both.

applicant_A={"python","docker","html","css","linux"}
applicant_B={"python","docker", "aws" ,"html","css"}
both=applicant_A.symmetric_difference(applicant_B)
print(both)

            #Check if one set is a subset of another. Example: Verifying if all registered workshop participants are also registered for the main conference
participants_A=["abhi","jiya","shivi","diya"]
participants_b={"diya","jiya"}
print(participants_b.issubset(participants_A))

                # Check if two sets are disjoint. Example: Checking if the set of morning shift workers and night shift workers have no common employees.

night_worker={"abhi","jiya","shivi","anuj"}
morning_worker={"anu","manu","diya","dishi"}
print(night_worker.isdisjoint(morning_worker))

                # Freeze a set. Example: Storing a fixed set of country codes that should never be modified.

constant=frozenset({22,14,56,78,98,21,60})
# constant.add(100)
print(constant)






