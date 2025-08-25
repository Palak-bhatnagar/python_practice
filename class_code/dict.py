student={
    "name":"shivi",
    "address":"meerut",
    "roll_no": 25,
    "teachers":["jiya","diya","akshara"],
    "subject":{
        "jiya":"maths",
        "diya":"history",
        "akshara":"hindi"
    },
}
student["book"]="jiya"
print(student)
print(student["roll_no"])
    # a=student["teachers"]
    # print(a[1])

print(student["teachers"][1]) 


print(student["subject"].items())
for teacher,sub in student["subject"].items():
    if teacher=="diya":
        print(f"{teacher}-{sub}")


print(student["subject"]["diya"])
print(student["subject"].get("jiya"))
# o=student["subject"].keys()
# print(o)

for sub in student["subject"].items():
    if sub[0]=="diya":
     print(f"{sub}")
     continue




