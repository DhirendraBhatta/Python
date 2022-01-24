#Comparision between for and while loop.Both prints the same result.
people=['Dhirendra','Bhatta']
for name in people:
    print(name)
print()

index=0
while index<len(people):
    print(people[index])
    index=index+1