#start: variables
a= 100
b= "naylathutu"
c= 99.9
print (a) 
print (b)
print (c)
del(a)
#print(a)

#Multiple Assignment 
a=b=c=100
print(a)
print(b)
print(c)

a,b,c = 100,11,"hellobody"
print(a)
print(b)
print(c)

#Local Variables
def sum(x,y):
    sum =x+y
    return sum
print(sum(1, 3))



def Function():
    # local variable
    insite = "insite funtion"
    print(insite)
Function()

# Global Variables
global_variables =12
def total():
    global global_variables
    global_variables=13
    a = global_variables
    return a 
print(total())

s = "global variables"
def myFunction():
    print("Inside myFunction", s)

myFunction()
print("Outside myFunction", s)

#nonlocal
def outerFunction():
  i = "today"
  def innerFunction():
    nonlocal i
    i = i + " Saturday"
    print(i)
  innerFunction()
outerFunction()