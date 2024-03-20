#1) Write a short Python script which queries the user for input (infinite loop with exit possibility) and writes the input to a file.
#2) Add another option to your user interface: The user should be able to output the data stored in the file in the terminal.
#3) Store user input in a list (instead of directly adding it to the file) and write that list to the file – both with pickle and json.
#4) Adjust the logic to load the file content to work with pickled/ json data.
import json
import pickle

def get_user_choice():
    return input('Enter your name: ')

waiting_for_input_json = True
waiting_for_input_pickle = True
list_names_json = []
list_names_pickle = []


while waiting_for_input_json:
    print('q - Quit')
    print('p - Print list')
    user_choice = get_user_choice()
    if user_choice == 'q':
        break
    if user_choice == 'p':
        with open('name.txt', mode='r') as f:
            # USING JSON 
            file_content = json.loads(f.read())
            for line in file_content:
                print('Your name is: {}'.format(line))
    else: 
        with open('name.txt', mode='w') as f:
            list_names_json.append(user_choice)
            # USING JSON 
            f.write(json.dumps(list_names_json))
   
            
            
while waiting_for_input_pickle:
    print('q - Quit')
    print('p - Print list')
    user_choice = get_user_choice()
    if user_choice == 'q':
        break
    if user_choice == 'p':
        with open('name.p', mode='rb') as f:
            # USING PICKLE 
            file_content = pickle.loads(f.read())
            for line in file_content:
                print('Your name is: {}'.format(line))

    else: 
        with open('name.p', mode='wb') as f:
            list_names_pickle.append(user_choice)
            # USING PICKLE
            f.write(pickle.dumps(list_names_pickle))
    



        
    