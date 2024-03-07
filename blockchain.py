
# Initializing our blockchain list

blockchain = []


def get_last_blockchain_value():
    """ Returns the last value of current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transation(transaction_amount, last_transaction = [1]): 
    """ Apend a new value as well as the last blockchain value to the blockchain. 
    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default[1]).
    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])
 

def get_transation_value():
    """ Returns the input of the user (a new transaction amount) as a float"""
    return float(input('Your transaction amount please: '))


def get_user_choice():
    return input('Your choice: ')
   
def print_blockchain_elements(): 
    for block in blockchain: 
        print('Outputting Block')
        print(block)
    else: 
        print('-' * 20)

def verify_chain():
    is_valid = True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue # if block index is 0, skip this iteration
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
                is_valid = True
        else: 
                is_valid = False
    return is_valid
    
tx_amount = get_transation_value()
add_transation(tx_amount)

waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transation_value()
        add_transation(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
      print_blockchain_elements()
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else: 
        print('Wrong value')
    if not verify_chain():
        print_blockchain_elements()
        print ('Invalid blockchain!')
        break
else: 
    print('User left!')
    
    
print('Done')
# break - exit loop before it's finished
# continue - skip current iteration