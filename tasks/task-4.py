import functools

# 1) Write a normal function that accepts another function as an argument. Output the result of that other function in your “normal” function.
# 2) Call your “normal” function by passing a lambda function – which performs any operation of your choice – as an argument.
# 3) Tweak your normal function by allowing an infinite amount of arguments on which your lambda function will be executed.    
# 4) Format the output of your “normal” function such that numbers look nice and are centered in a 20 character column.


def print_sum(calculate_sum, *args): # *args allows to pass more parameters
    for arg in args: 
        print('Your number is: {:^20.2f}'.format(calculate_sum(arg))) 
    
print_sum(lambda amount: amount * 2, 20, 30, 11)