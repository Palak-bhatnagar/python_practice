# def lowercase(text):
#     return text.lower()

# def uppercase(text):
#     return text.upper()

# def sentence(x):
#     name= x("hello world!!")
#     return name

# print(sentence(uppercase))
    



                            # NOTIFICAATION SYSTEM

# def email(message):
#     print(f"email : {message}")

# def upi(message):
#     print(f"upi : {message}")

# def paypal(message):
#     print(f"paypal : {message}")

# def main(sending_func, message):
#     sending_func(message)

# main(email,"you recieved your product")
# main(upi,"you recieved your product")
# main(paypal,"you recieved your product")



                             # Data processing

def clean_data(x):
    return x.strip()

def capital_data(x):
    return x.title()

def greet(name,x):
   return name(x)

print(greet(clean_data,"  hello world  "))
print(greet(capital_data,"  hello world  "))





