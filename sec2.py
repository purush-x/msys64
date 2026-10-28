import hashlib
from argon2 import PasswordHasher

password = "1234"

md5_hash = hashlib.md5(password.encode()).hexdigest()
sha256_hash = hashlib.sha256(password.encode()).hexdigest()

ph = PasswordHasher()
argon2_hash = ph.hash(password)

print("Original Password:", password)
print("MD5 hash:", md5_hash)
print("SHA256 hash:", sha256_hash)
print("Argon2 hash:", argon2_hash)