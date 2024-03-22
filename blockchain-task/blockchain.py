
from functools import reduce
import hashlib as hl
from collections import OrderedDict
import json
import pickle

from hash_util import hash_string_256, hash_block

# Initializing our blockchain list
MINING_REWARD = 10
blockchain = []
open_transactions = []
owner = 'Ola'
participants = {'Ola'} # usage of set



def load_data():
    """Initialize blockchain + open transactions data from a file."""
    global blockchain
    global open_transactions
    try:
        with open('blockchain.txt', mode='r') as f:
            # file_content = pickle.loads(f.read())
            file_content = f.readlines()
            # blockchain = file_content['chain']
            # open_transactions = file_content['ot']
            blockchain = json.loads(file_content[0][:-1])
            # We need to convert  the loaded data because Transactions should use OrderedDict
            updated_blockchain = []
            for block in blockchain:
                updated_block = {
                    'previous_hash': block['previous_hash'],
                    'index': block['index'],
                    'proof': block['proof'],
                    'transactions': [OrderedDict(
                        [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])]) for tx in block['transactions']]
                }
                updated_blockchain.append(updated_block)
            blockchain = updated_blockchain
            open_transactions = json.loads(file_content[1])
         # We need to convert  the loaded data because Transactions should use OrderedDict
            updated_transactions = []
            for tx in open_transactions:
                updated_transaction = OrderedDict(
                    [('sender', tx['sender']), ('recipient', tx['recipient']), ('amount', tx['amount'])])
                updated_transactions.append(updated_transaction)
            open_transactions = updated_transactions
    except (IOError): # which error I want to handle - FileNotFoundError is part of IOError error
        genesis_block = {'previous_hash': '', 'index': 0, 'transactions': [], 'proof': 100}
        blockchain = [genesis_block]
        open_transactions = []
    finally: # it always run
        print('Cleanup!')

load_data()

def save_data():
    try:
        with open('blockchain.txt', mode='w') as f: # if wb - write binary, blockchain.p - if wb
            # SOLUTION WITH JSON
            f.write(json.dumps(blockchain))
            f.write('\n')
            f.write(json.dumps(open_transactions))
        
            # SOLUTION WITH PICKLE 
            # save_data = {
            #     'chain': blockchain,
            #     'ot': open_transactions
            # }  it's created because we can't add text like \n, because we store binary data. it's better to create dictionary that stores all the data I want to pickle
            # f.write(pickle.dumps(save_data)) 
    except IOError:
        print('Saving failed!')
        
        
def valid_proof(transactions, last_hash, proof): 
    guess = (str(transactions) + str(last_hash) + str(proof)).encode()
    print(guess)
    guess_hash = hash_string_256(guess)
    print(guess_hash)
    return guess_hash[0:2] == '00'


def proof_of_work():
    last_block = blockchain[-1]
    last_hash = hash_block(last_block)
    proof = 0
    while not valid_proof(open_transactions, last_hash, proof):
        proof += 1
    return proof

    
def get_balance(participant):
    tx_sender = [[tx['amount'] for tx in block['transactions'] if tx['sender'] == participant] for block in blockchain] # nested list comprehensions
    open_tx_sender = [tx['amount'] for tx in open_transactions if tx['sender'] == participant]
    tx_sender.append(open_tx_sender)
    amount_sent = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_sender, 0)
    tx_recipient = [[tx['amount'] for tx in block['transactions'] if tx['recipient'] == participant] for block in blockchain]
    amount_received = reduce(lambda tx_sum, tx_amt: tx_sum + sum(tx_amt) if len(tx_amt) > 0 else tx_sum + 0, tx_recipient, 0)
    return amount_received - amount_sent
    
    
def get_last_blockchain_value():
    """ Returns the last value of current blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def verify_transaction(transaction):
    sender_balance = get_balance(transaction['sender'])
    return sender_balance >= transaction['amount']


def add_transation(recipient, sender=owner, amount=1.0): 
    """ Apend a new value as well as the last blockchain value to the blockchain. 
    Arguments:
        :sender: The sender of the coins.
        :recipient: The recipient of the coins.
        :amount: The amount of coins sent with transaction (default = 1.0)
    """
    # transaction ={'sender': sender, 'recipient': recipient, 'amount': amount} --> It can't be dictionary because we care about order and dictionaries may have random order
    transaction = OrderedDict([('sender', sender), ('recipient', recipient), ('amount', amount)]) # To have always the same order, you can use OrderDict
    if verify_transaction(transaction):
        open_transactions.append(transaction)
        participants.add(sender) # adding to set
        participants.add(recipient) # adding to set
        save_data()
        return True
    return False
    
 
def mine_block():
    last_block = blockchain[-1]
    hashed_block = hash_block(last_block)
    proof = proof_of_work()
    reward_transaction = OrderedDict([('sender', 'MINING'), ('recipient', owner), ('amount', MINING_REWARD)])
    copied_transaction = open_transactions[:]
    copied_transaction.append(reward_transaction)
    block = {'previous_hash': hashed_block, 'index': len(blockchain), 'transactions': copied_transaction, 'proof': proof}
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
        if not valid_proof(block['transactions'][:-1], block['previous_hash'], block['proof']):
            print('Proof of work is invalid')
            return False
    return True

def verify_transactions():
    return all([verify_transaction(tx) for tx in open_transactions])


waiting_for_input = True

while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction value')
    print('2: Mine a new block')
    print('3: Output the blockchain blocks')
    print('4: Output participants')
    print('5: Check transaction validity')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_data = get_transation_value()
        recipient, amount = tx_data # refering to tuple - we pull out first value of the tuple and store in 'recipient' variable, and the second value - store in 'amount' value
        if add_transation(recipient, amount=amount):
            print('Added transaction!')
        else:
            print('Transaction failed!')
        print(open_transactions)
    elif user_choice == '2':
        if mine_block():
            open_transactions = []
            save_data()
    elif user_choice == '3':
      print_blockchain_elements()
    elif user_choice == '4':
      print(participants)
    elif user_choice == '5':
      if verify_transactions():
          print('All transactions are valid')
      else:
           print('There are invalid transactions')
    elif user_choice == 'h':
        if len(blockchain) >=1:
            blockchain[0] = {'previous_hash': '', 'index': 0, 'transactions': [{'sender': 'Kuba', 'recipient': 'Agnieszka', 'amount': 2.0}]}
    elif user_choice == 'q':
        waiting_for_input = False
    else: 
        print('Wrong value')
    if not verify_chain():
        print_blockchain_elements()
        print ('Invalid blockchain!')
        break
    print('Balance of {}: {:6.2f}'.format('Ola', get_balance('Ola')))
else: 
    print('User left!')
    
    
print('Done')
# break - exit loop before it's finished
# continue - skip current iteration