from Crypto.PublicKey import RSA
import Crypto.Random
import binascii
from Crypto.Signature import PKCS1_v1_5 # alghoritm that generates signatures
from Crypto.Hash import SHA256

class Wallet:
    def __init__(self, node_id):
        self.private_key = None
        self.public_key = None
        self.node_id = node_id
        
    def create_keys(self):
        private_key, public_key = self.generate_keys()
        self.private_key = private_key
        self.public_key = public_key

    
    def save_keys(self):
        """Saves the keys to a file (wallet.txt)."""
        if self.public_key != None and self.private_key != None:
            try:
                with open('wallet-{}.txt'.format(self.node_id), mode='w') as f:
                    f.write(self.public_key)
                    f.write('\n')
                    f.write(self.private_key)
                return True
            except (IOError, IndexError):
                print('Saving wallet failed...')
                return False
            
    
    def load_keys(self):
        """Loads the keys from the wallet.txt file into memory."""
        try:
            with open('wallet-{}.txt'.format(self.node_id), mode='r') as f:
                keys = f.readlines()
                public_key = keys[0][:-1]
                private_key = keys[1]
                self.public_key = public_key
                self.private_key = private_key
            return True
        except (IOError, IndexError):
            print('Loading wallet failed...')
            return False
 
    
    def generate_keys(self):
        private_key = RSA.generate(1024, Crypto.Random.new().read) # returns private keys, 1024 - number of bits
        public_key = private_key.public_key() # public key is created from private key
        return (binascii.hexlify(private_key.exportKey(format='DER')).decode('ascii'), binascii.hexlify(public_key.exportKey(format='DER')).decode('ascii')) # keys are in binary format so I need to convert them, format='DER' - binary encoding, ascii - characters
    
    
    def sign_transaction(self, sender, recipient, amount):
        signer = PKCS1_v1_5.new(RSA.import_key(binascii.unhexlify(self.private_key))) # binascii.unhexlify - turns string into binary format
        h = SHA256.new((str(sender) + str(recipient) + str(amount)).encode('utf8')) # creates a hash
        signature = signer.sign(h)
        return binascii.hexlify(signature).decode('ascii')
    
    @staticmethod
    def verify_transaction(transaction):
        public_key = RSA.import_key(binascii.unhexlify(transaction.sender))
        verifier = PKCS1_v1_5.new(public_key)
        h = SHA256.new((str(transaction.sender) + str(transaction.recipient) + str(transaction.amount)).encode('utf8'))
        return verifier.verify(h, binascii.unhexlify(transaction.signature))