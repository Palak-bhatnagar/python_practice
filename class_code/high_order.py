def lowercase(text):
    return text.lower()

def uppercase(text):
    return text.upper()

def sentence(x):
    name= x("hello world!!")
    return name

print(sentence(uppercase))
    



                            # NOTIFICAATION SYSTEM

def email(message):
    print(f"email : {message}")

def upi(message):
    print(f"upi : {message}")

def paypal(message):
    print(f"paypal : {message}")

def main(sending_func, message):
    sending_func(message)

main(email,"you recieved your product")
main(upi,"you recieved your product")
main(paypal,"you recieved your product")



                             # Data processing

# def clean_data(x):
#     return x.strip()

# def capital_data(x):
#     return x.title()

# def greet(name,x):
#    return name(x)

# print(greet(clean_data,"  hello world  "))
# print(greet(capital_data,"  hello world  "))





# def louder(l):
#     print(l.upper())
# def softer(s):
#     print(s.lower())
# def speak(func):
#     func("HELLO there")
# speak(louder)
# speak(softer)



# def greet_louder(name):
#     print(f"hii {name.upper()}")
# def greet_softer(name):
#     print(f"hii {name.lower()}")
# def greet_hello(other_func,names):
#     other_func(names)

# greet_hello(greet_louder,"palak")


# def shout(text):
#     return text.upper()
# def up(text):
#     return text.lower()
# def greet(other_func,mes):
#     message=other_func(mes)
#     print(message)

# greet(shout,"HEYY shouting")
# greet(up,"HEYY shouting")



                                       # Example 2 – Returning a function


def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier  # returning a function
print(make_multiplier(3))
times3 = make_multiplier(3)
print(times3(5))  # 15


# make_multiplier(3)
#    ↓
# Returns function multiplier(x)  (but remembers n = 3)
#    ↓
# times3 is now multiplier(x) with n fixed at 3
#    ↓
# times3(5) → 5 * 3 = 15

def cbse(n):
    def marks(m1,m2,m3,m4,m5):
        return m1+m2+m3+m4+m5+n
    return marks
total=cbse(10)
print(total(1,2,4,3,6))






