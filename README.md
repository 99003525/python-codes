class trial():
    def add(*args):
        print("sum of given values :", sum(args))
        print("end of class trial ")
s=trial
print(type(s))
s.add(10,30,40)


def org(**inputs):
    print(type(inputs))
    for i in inputs.keys():
        print("keys are:",i )
    for j in inputs.values():
        print("values are:",j)
    print("end of multi-keyword arguements")
    
org(b=10,a=20,f=50)


def multiply(*inputs):
    product = 1
    print(type(inputs))
    for i in inputs:
        product=product*i
    print("end of multiple arguements")
    return product

    
s=multiply(10,20,30)
print(type(s))
print(s)
