"""Python tools for cryptography (not the lib cryptography, the thing in general.)"""
import cryptography.fernet as fernetlib
import base64
#import hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256 as crypto_sha256

def password_to_fernet_key(password: str, salt: bytes) -> bytes:
    kdf = PBKDF2HMAC(
        algorithm=crypto_sha256(),
        length=32, 
        salt=salt,
        iterations=100_000,
    )
    
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)

def password_to_fernet_key_nosalt(password: str) -> bytes:
    """Insecure but simpler version of password_to_fernet_key. DO NOT USE FOR IMPORTANT DATA!! USE password_to_fernet_key() INSTEAD."""
    salt = "beeaf470da107182d1b237f4dfe5ffbcd2ce276a2ad4056151e202855f2f388e".encode()
    kdf = PBKDF2HMAC(
        algorithm=crypto_sha256(),
        length=32, 
        salt=salt,
        iterations=100_000,
    )
    
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)