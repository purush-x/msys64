import hashlib
import bcrypt
from argon2 import PasswordHasher

password = "1234"

md5_hash = hashlib.md5(password.encode()).hexdigest()
sha256_hash = hashlib.sha256(password.encode()).hexdigest()
bcrypt_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
argon2_hash = PasswordHasher().hash(password)

print("MD5 hash:", md5_hash)
print("SHA256 hash:", sha256_hash)
print("Argon2 hash:", argon2_hash)
print("Bcrypt hash:", bcrypt_hash.decode())