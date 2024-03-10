#1) Create a list of names and use a for loop to output the length of each name (len() ).
#2) Add an if  check inside the loop to only output names longer than 5 characters.
#3) Add another if  check to see whether a name includes a “n”  or “N”  character.
#4) Use a while  loop to empty the list of names (via pop() )

names = ['Ola', 'Ania', 'Karolina', 'Natalia']

for name in names:
    print(name + ' - ' + str(len(name)) + ' letters')
    if len(name) > 5 and 'n' in name.lower():
        print(name + ' has more than 5 characters and includes `n`')

while len(names) != 0:
    names.pop()
    