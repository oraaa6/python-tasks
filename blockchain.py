
# Initializing our blockchain list
genesis_block = {'previous_hash': '', 'index': 0, 'transictions': []}
blockchain = [genesis_block]
open_transations = []
owner = 'Ola'
participants = {'Ola'} # usage of set

def hash_block(block):
    return '-'.join([str(block[key]) for key in block]) # usage of list comprehensions with dictionary //  '-'.join([str(last_block[key]) for key in last_block]) takse list as an argument an join by character (here: -)
    
    
def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transictions'] if tx['sender'] == participant] for block in blockchain] # nested list comprehensions
    amount_sent = 0
    for tx in tx_sender:
        if len(tx) > 0:
            amount_sent+= tx[0]
    tx_recipient = [[tx['amount'] for tx in block['transictions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = 0
    for tx in tx_recipient:
        if len(tx) > 0:
            amount_received+= tx[0]
    return amount_received - amount_sent
    
def get_last_blockchain_value():
    """ Returns the last value of current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_transation(recipient, sender=owner, amount=1.0): 
    """ Apend a new value as well as the last blockchain value to the blockchain. 
    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with transaction (default = 1.0)
    """
    transaction ={'sender': sender, 'recipient': recipient, 'amount': amount}  # Dictionary
    open_transations.append(transaction)
    participants.add(sender) # adding to set
    participants.add(recipient) # adding to set
 
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    block = {'previous_hash': hashed_block, 'index': len(blockchain), 'transictions': open_transations}
    blockchain.append(block)
    return True
 

def get_transation_value():
    """ Returns the input of the user (a new transaction amount) as a float"""
    tx_recipient = input('Enter the recipient of the transaction: ')
    tx_amount = float(input('Your transaction amount please: '))
    return tx_recipient, tx_amount # Tuple - when we have more than 1 value, we can omit (). Empty tulple - ()


def get_user_choice():
    return input('Your choice: ')
   
def print_blockchain_elements(): 
    for block in blockchain: 
        print('Outputting Block')
        print(block)
    else: 
        print('-' * 20)

def verify_chain():
    for (index, block) in enumerate(blockchain): # enumerate() gives back a tuple which contains two pieces of information: index and element
        if index == 0:
            continue
        if block['previous_hash'] != hash_block(blockchain[index - 1]):
            return False
    return True


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transation_value()
        recipient, amount = tx_data # refering to tuple - we pull out first value of the tuple and store in 'recipient' variable, and the second value - store in 'amount' value
        add_transation(recipient, amount=amount)
        print(open_transations)
    elif user_choice == '2':
        if mine_block():
            open_transations = []
    elif user_choice == '3':
      print_blockchain_elements()
    elif user_choice == '4':
      print(participants)
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[0] = {'previous_hash': '', 'index': 0, 'transictions': [{'sender': 'Kuba', 'recipient': 'Agnieszka', 'amount': 2.0}]}
    elif user_choice == 'q':
        waiting_for_input = False
    else: 
        print('Wrong value')
    if not verify_chain():
        print_blockchain_elements()
        print ('Invalid blockchain!')
        break
    print(get_balance('Ola'))
else: 
    print('User left!')
    
    
print('Done')
# break - exit loop before it's finished
# continue - skip current iteration