"""Provider verification helper methods. """ # it describes whole file

from utility.hash_util import hash_string_256, hash_block
from wallet import Wallet

class Verification:
    @staticmethod # valid_proof don't need anything from class, with static method we can't pass self
    def valid_proof(transactions, last_hash, proof): 
        guess = (str([tx.to_ordered_dict() for tx in transactions]) + str(last_hash) + str(proof)).encode()
        print(guess)
        guess_hash = hash_string_256(guess)
        print(guess_hash)
        return guess_hash[0:2] == '00'
    
    @classmethod # verify_chain need access to the class (it uses self) but don't need instance here, cls instead self is a convention
    def verify_chain(cls, blockchain):
        for (index, block) in enumerate(blockchain): # enumerate() gives back a tuple which contains two pieces of information: index and element
            if index == 0:
                continue
            if block.previous_hash != hash_block(blockchain[index - 1]):
                return False
            if not cls.valid_proof(block.transactions[:-1], block.previous_hash, block.proof):
                print('Proof of work is invalid')
                return False
        return True
    
    @staticmethod
    def verify_transaction(transaction, get_balance, check_funds=True):
        if check_funds == True:
            sender_balance = get_balance()
            return sender_balance >= transaction.amount and Wallet.verify_transaction(transaction)
        else: 
            return Wallet.verify_transaction(transaction)
    
    @classmethod # it needs to have an access something from class (here: verify_transaction) so it'll be classmethod
    def verify_transactions(cls, open_transactions, get_balance):
        return all([cls.verify_transaction(tx, get_balance, False) for tx in open_transactions])
    
        