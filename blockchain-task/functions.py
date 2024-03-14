def unlimited_arguments(*args, **keyword_args):  # * - take all arguments separated by commas and turn into a tuple list, ** - unpack dictionary
    for k, argument in keyword_args.items():
        print(k, argument)
        
unlimited_arguments(1,2,3,4, name="Kuba", age=25) # changes to (1, 2, 3, 4)