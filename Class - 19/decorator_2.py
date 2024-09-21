""" @testcase
def calc(a,b):
    print(a/b)

calc(20,2)
calc(10,0) """


""" def testcase(func) :
    def inner(a,b):
        if b==0:
            print("Can't Divided By Zero")
        else :
            return func(a,b)
    return inner


#@testcase
def calc(a,b):
    print(a/b)

calc(20,2)
calc(10,0) """



def testcase(func) :
    def inner(a,b):
        if b==0:
            print("Can't Divided By Zero")
        else :
            return func(a,b)
    return inner


@testcase
def calc(a,b):
    print(a/b)

calc(20,2)
calc(10,0)