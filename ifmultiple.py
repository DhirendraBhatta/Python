#Calculate the canadian sales tax rate on the basis of following conditions:
#For the province Alberta,Nunuvut or Yukon,charge 5%
#For the province Ontario,charge 13%
#For all the other provinces,charge 15%
country=input('Enter the country name\n')
if country.lower()=='canada':
    print('You are a Canadian and You have to pay sales tax')
    province=input('Enter the province name\n')
    if province.capitalize() in ('Alberta','Nunavut','Yukon'):
        tax=.05
    elif province.capitalize()== 'Ontario':
        tax=.13
    else:
        tax=.15
    print('The tax rate of '+ str.capitalize(province)+ ' is '+ str(tax))
else:
    tax=0
    print('You are not a Canadian')
    print('You have to pay '+ str(tax)+ ' sales tax.')