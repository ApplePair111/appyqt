"""Python tools for cryptography (not the lib cryptography, the thing in general.)"""
import cryptography.fernet as fernetlib
import base64
#import hashlib
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives.hashes import SHA256 as crypto_sha256

def password_to_fernet_key(password: str, salt: bytes) -> bytes:
    """Turns a password and a salt to a Fernet key."""
    kdf = PBKDF2HMAC(
        algorithm=crypto_sha256(),
        length=32, 
        salt=salt,
        iterations=100_000,
    )
    
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)

def password_to_fernet_key_nosalt(password: str) -> bytes:
    """Insecure but simpler version of password_to_fernet_key. DO NOT USE FOR IMPORTANT DATA!! USE password_to_fernet_key() INSTEAD. It's fine to use if you're not building something offline."""
    salt = "beeaf470da107182d1b237f4dfe5ffbcd2ce276a2ad4056151e202855f2f388e".encode()
    kdf = PBKDF2HMAC(
        algorithm=crypto_sha256(),
        length=32, 
        salt=salt,
        iterations=100_000,
    )
    
    key = kdf.derive(password.encode())
    return base64.urlsafe_b64encode(key)

def pwdEncrypt(password: str, data: str | bytes):
    """Encrypts a string or byte object with a password. use pwdDecrypt to decrypt."""
    fernetKey = password_to_fernet_key_nosalt(password)
    f = fernetlib.Fernet(fernetKey)

def pwdEncrypt(password: str, data: str | bytes):
    fernetKey = password_to_fernet_key_nosalt(password)
    f = fernetlib.Fernet(fernetKey)

    if isinstance(data, bytes):
        return f.encrypt(data)
    else:
        return f.encrypt(data.encode())
def pwdDecrypt(password: str, data: bytes):
    fernetKey = password_to_fernet_key_nosalt(password)
    f = fernetlib.Fernet(fernetKey)
    return f.decrypt(data)