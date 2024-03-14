
# 1) Create two variables – one with your name and one with your age

user_name = input('Please enter your name: ')
user_age = input('Please enter your age: ')

# 2) Create a function which prints your data as one string

def print_user():
    """ Prints user data """
    print(user_name + ', ' + user_age)

print_user()

# 3) Create a function which prints ANY data (two arguments) as one string
    
user_salary = input('Please enter your salary: ') 

def print_salary(salary, currency = 'PLN'):
    print(salary + currency)

print_salary(user_salary)

# 4) Create a function which calculates and returns the number of decades you already lived (e.g. 23 = 2 decades)

decade = 10

def calculate_decades():
     return int(float(user_age)/decade)
    
print(calculate_decades())