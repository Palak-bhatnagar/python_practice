#                                     # payment processing
# def pay_with_card(money):
#     print("payment with card is processing for:", money) 
# def pay_with_UPI(money):
#     print("payment with upi is processing for:", money)
# def pay_with_paypal(money):
#     print("payment with paypal is processing for:", money)
# def payment(product,amount):
#     product(amount)

# payment(pay_with_UPI,900)
# payment(pay_with_card,300)
# payment(pay_with_paypal,600)


# def make_multiplier(n):
#     def multiplier(x):
#         return x* n
#     return multiplier
# time=make_multiplier(3)
# print(time(5))

#                         # Convert prices from USD to INR

# prices_usd = [10, 25, 50, 100]
# # a=list(map(lambda v:v*83,prices_usd))
# # print(a)

# def convert(usd):
#     return usd *83
# # print(convert(prices_usd))


#                             # Make all names uppercase

# names = ["Alice", "Bob", "Charlie"]
# b=list(map(lambda x:x.upper(),names))
# print(b)

#                             # numbers = [1, 2, 3, 4, 5, 6] using filter()
# numbers = [1, 2, 3, 4, 5, 6]                            
# c=list(filter(lambda x:x%2==0,numbers))
# print(c)

#                             # students who passed

# scores = [45, 78, 32, 90, 55]
# def passed(x):
#     return x>=50
# d=list(filter(passed,scores))
# print(d)

                            # Sort names by length

# def ceo(salary):
#     a= salary * (10/100)
#     return salary+a
# def software_e(salary):
#     a =salary * (10/100)
#     return salary+a
# def manager(salary):
#     a=salary * (10/100)
#     return salary+a
# def inc(employee,salary):
#     return employee(salary)
# print(inc(ceo,12000))
# print(inc(manager,20000))

def emp(n):
    def inc(x):
        a=n*(x/100)
        return n+a
    return  inc
salary=emp(12000)
print(salary(10))