#Input command also returns the string while doing concatenation.Type conversion needed for int and float.
# first='5'
# second='6'
# first=input('Enter first number ')
# second=input('Enter second number ')

first=input('Enter first number ')
second=input('Enter second number ')
#This input command concatenates or joins the two numbers as a string character(IF first=5,second=6 then, result=56)
print(first + second)
#This is the type conversion of string input to integer.
print(int(first) + int(second))
#This is the type conversion of string into float or decimal.
print(float(first)+float(second))
