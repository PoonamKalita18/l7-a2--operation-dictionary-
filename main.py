#empty dictionary
D = {}

D = {1:'Poonam', 2: 'Yoongi'}

D= {'name':'Kaliya', 'age': 30}
D= {'name': 'Jack', 1:[2,4,3]}

#output
print(D['name'])
print(D.get('age'))

#updating
D['age']=  15
print(D)

#add elements
D['address']= 'Guwahati'

#removing
D.pop('age')
print(D)

#accesing an element
print('address:', D.get('address'))

#removing all the elements
D.clear()
print(D)