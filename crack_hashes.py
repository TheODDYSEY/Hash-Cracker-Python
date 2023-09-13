
import hashlib
from tqdm import tqdm

# List of supported hash types
hash_names = [
    'blake2b', 
    'blake2s', 
    'md5', 
    'sha1', 
    'sha224', 
    'sha256', 
    'sha384', 
    'sha3_224', 
    'sha3_256', 
    'sha3_384', 
    'sha3_512', 
    'sha512',
]