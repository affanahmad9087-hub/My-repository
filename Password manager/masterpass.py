import os
import base64
import json
import hashlib

MASTER_FILE = "master.dat"

#checks whether the file is created or not
def master_exists():
    return os.path.exists(MASTER_FILE)

#creates the password
def create_master_password(password : str):
    salt = os.urandom(16)  # adds some salt to the hash of the password
    # using PBKDF2_HMAC to apply salt, hashing algorithm, and number of iterations.
    hash_bytes = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        200000
    )

    #stores the salt and the hash in dictionary format.
    data = {
        "salt" : base64.b64encode(salt).decode(),
        "hash" : base64.b64encode(hash_bytes).decode()
    }

    #dumps the stored salt and hash to the file for access
    with open(MASTER_FILE, "w") as f:
        json.dump(data, f)

#checks the inputted password
def verify_master_password(password : str):
    if not master_exists():
        return False

    #with the file open, it loads the salt and hash
    with open(MASTER_FILE, "r") as f:
        data = json.load(f)

    salt = base64.b64decode(data["salt"])# salt loading
    stored_hash = base64.b64decode(data["hash"])# hash loading
    
    #recompute hash
    hash_bytes = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        200000
    )

    return hash_bytes == stored_hash



