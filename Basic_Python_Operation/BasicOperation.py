#Python Arithmetic
a = 10
b = 20
c = a+b #Addition
print(c)
print(a-b) #Subtraction
print(a*b) #Multiplication
print(a**b) #Exponent or power
print(a/b) #Division
print(b//a) #Floor Division decimal points are removed

##### String Operations #####
print("----String Operation----")
a = "Kunal Raj"
b = "Bhardwaj"
c = a+b #Concatenation

print("String Concatenation of "+a+" and "+b+" is :"+c)
d = """This is a test, please note it down""" #Multiple String to be printed in same order
print("Printing text in desired pattern ::\n :"+d)

e = '''This is,
test. See the difference''' #Same as above (Multiple String)
print(e)

#String are array of bytes representing unicode character
print("String AS Array :\n")
f = "Test"
print("Character at 0th position of "+f+" is : "+f[0])
print("\nString Slicing : "+f[1:3])
print("\nString Slicing from last : "+f[-3:-1])
print("Length of "+f+" is ")
print(len(f))

print("String and int concatenation :"+"Lengh of "+f+" is : "+str(len(f)))
u ="Length is : {}"
print(u.format(len(f)))

print("\n\nRemoving leading and triling spaces : ")
g = " Hello, World "
print("With space:"+g)
print("Without space :"+g.strip())
print("Without left space:"+g.lstrip())
print("Without Right space:"+g.rstrip())

#Changing to Upper or lower case
h = "Hello, World"
print("\n\n"+h)
print("Lower case : "+h.lower())
print("Upper case : "+h.upper())

#Relacing a character in  string 
print("\n\nReplacing H with K in Hello, World : "+h.replace("H","K"))

#Spliting string with comma and converting it into list
print("After Splitting : "+ str(h.split(",")))

if __name__ == '__main__' :
    print("Test")
    print("Out")