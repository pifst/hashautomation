from passlib.hash import pbkdf2_sha256

input = input("Input string to be hashed: ")
hash = pbkdf2_sha256.hash(input)

print(hash)