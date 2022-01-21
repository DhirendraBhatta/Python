x=100
y=0
try:
    print(x/y)
except ZeroDivisionError as e:
    #Optionally,log e somewhere
    print('Not allowed to divide by zero')
else:  
    print('Something really went wrong')
finally:
    print('This always runs on success or failure.This is our cleanup code')
