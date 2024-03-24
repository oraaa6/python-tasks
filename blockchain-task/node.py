from blockchain import Blockchain
from uuid import uuid4
from verification import Verification

class Node:
    
    def __init__(self):
        # self.id = str(uuid4())
        self.id = 'Ola'
        self.blockchain = Blockchain(self.id)
            
    def listen_for_input(self):
        waiting_for_input = True
        while waiting_for_input:
            print('Please choose')
            print('1: Add a new transaction value')
            print('2: Mine a new block')
            print('3: Output the blockchain blocks')
            print('4: Check transaction validity')
            print('q: Quit')
            user_choice = self.get_user_choice()
            if user_choice == '1':
                tx_data = self.get_transation_value()
                recipient, amount = tx_data # refering to tuple - we pull out first value of the tuple and store in 'recipient' variable, and the second value - store in 'amount' value
                if self.blockchain.add_transation(recipient,self.id ,amount=amount):
                    print('Added transaction!')
                else:
                    print('Transaction failed!')
                print(self.blockchain.get_open_transactions())
            elif user_choice == '2':
                self.blockchain.mine_block()
            elif user_choice == '3':
                self.print_blockchain_elements()
            elif user_choice == '4':
                if Verification.verify_transactions(self.blockchain.open_transactions, self.blockchain.get_balance):
                    print('All transactions are valid')
                else:
                    print('There are invalid transactions')
            elif user_choice == 'q':
                waiting_for_input = False
            else: 
                print('Wrong value')
            if not Verification.verify_chain(self.blockchain.chain):
                self.print_blockchain_elements()
                print ('Invalid blockchain!')
                break
            print('Balance of {}: {:6.2f}'.format(self.id, self.blockchain.get_balance()))
        else: 
            print('User left!')
        print('Done')
        
        
    def get_transation_value(self):
        """ Returns the input of the user (a new transaction amount) as a float"""
        tx_recipient = input('Enter the recipient of the transaction: ')
        tx_amount = float(input('Your transaction amount please: '))
        return tx_recipient, tx_amount # Tuple - when we have more than 1 value, we can omit (). Empty tulple - ()


    def get_user_choice(self):
        return input('Your choice: ')
   
    def print_blockchain_elements(self): 
        for block in self.blockchain.chain(): 
            print('Outputting Block')
            print(block)
        else: 
            print('-' * 20)
            
node = Node()
node.listen_for_input()