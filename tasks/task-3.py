
#1) Create a list of “person” dictionaries with a name, age and list of hobbies for each person. Fill in any data you want.
#2) Use a list comprehension to convert this list of persons into a list of names (of the persons).
#3) Use a list comprehension to check whether all persons are older than 20.
#4) Copy the person list such that you can safely edit the name of the first person (without changing the original list).
#5) Unpack the persons of the original list into different variables and output these variables.

persons = [
    {'name': 'Kuba', 'age': 19, 'hobbies': ['sport', 'dancing' ]}, 
    {'name': 'Anna', 'age': 23, 'hobbies': ['cooking', 'travelling' ]}, 
    {'name': 'Karolina', 'age': 28, 'hobbies': ['cycling', 'running' ]}
    ]

names_list = [el['name'] for el in persons]
print(names_list)

are_older = all([el['age'] > 20 for el in persons])
print(are_older)

copy_persons = [el.copy() for el in persons]
copy_persons[0]['name'] = 'Agnieszka'
print(copy_persons)
print(persons)

person_a, person_b, person_c = persons
print(person_a['name'])
print(person_b['name'])
print(person_c['name'])
