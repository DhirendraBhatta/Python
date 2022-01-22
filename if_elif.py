province=input('Enter the province of Canada\n')
if province.capitalize()=='Alberta':
    tax=.05
elif province.capitalize()=='Nunavut':
    tax=.05
elif province.capitalize()=='Ontario':
    tax=.13
else:
    tax=.15
print('The tax rate is : '+ str(tax))
