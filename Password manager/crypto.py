#This file will contain:
#-key generation
#-encryption
#-decryption
#-password derivation

# we will fill this in stage 3

import os
import base64
from typing import Tuple

import cryptography
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet, InvalidToken

KDF_ITERATIONS = 200_000
SALT_SIZE = 16  #bytes


def derive_key(password: str, salt: bytes | None = None) -> Tuple[bytes, bytes]:
    """

    Derive a Fernet-compatible key from a password using PBKDF2-HMAC-SHA256.

    Args:
        password: the master password (string)
        salt: optional 16 byte salt. If None, a new random salt is generated.

    Returns:
        (fernet_key, salt)
        - fernet_key is a 32-byte base64 urlsafe key (bytes) usable with cryptography.Fernet
        - salt is the random salt used
    """

    if salt is None:
        salt = os.urandom(SALT_SIZE)

    # PBKDF2HMAC to derive 32 bytes (256 bits) for Fernet
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=KDF_ITERATIONS,
        backend=default_backend(),
    )
    key = kdf.derive(password.encode("utf-8"))  # raw bytes

    # fernet expects an urlsafe_base64-encoded 32 byte key
    fernet_key = base64.urlsafe_b64encode(key)
    return fernet_key, salt


def encrypt_bytes(fernet_key: bytes, plaintext: bytes) -> bytes:
    """
    Encrypt plaintext bytes using Fernet(AES-128 in CBC + HMAC; safe)
    Returns token bytes (contains IV, ciphertext, HMAC etc.)
    """

    f = Fernet(fernet_key)
    token = f.encrypt(plaintext)
    return token


def decrypt_bytes(fernet_key: bytes, token: bytes) -> bytes:
    """
    Decrypt a Fernet token. Raises cryptography.fernet.InvalidToken on failure.
    """
    f = Fernet(fernet_key)
    try:
        plaintext = f.decrypt(token)
    except InvalidToken as e:
        #Re-raise so that callers can handle it.
        raise
    return plaintext
