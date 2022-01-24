#This is a dictionary similar like words and their definitions
dhirendra={}
dhirendra['first']='Dhirendra'
dhirendra['last']='Bhatta'
print(dhirendra)
#Press ctrl+D in VS code to replace the selected text with another name
sujal={}
sujal['first']='Sujal'
sujal['last']='Bohara'
print(sujal)
#List has the collection of dictionaries too separated by comma.
people=[]
people.append(dhirendra)
people.append(sujal)
#This will add the below dictionary in the last of the list
people.append({
    'first':'Sulav','last':'Bohara'
})
people.append({
    'first':'Bill','last':'Gates'
})
#people=[dhirendra,sujal]
print(people)