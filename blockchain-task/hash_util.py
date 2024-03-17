import hashlib as hl
import json

def hash_string_256(string):
    return hl.sha256(string).hexdigest()

def hash_block(block):
    return hash_string_256(json.dumps(block, sort_keys=True).encode()) # hexdigest convert binary string into a string, sha256 - algorithm that creates hash, json.dumbs - convert dictionary, encode - encode utf-8
    # return '-'.join([str(block[key]) for key in block]) # usage of list comprehensions with dictionary //  '-'.join([str(last_block[key]) for key in last_block]) takse list as an argument an join by character (here: -)