from passlib.hash import pbkdf2_sha256

filename = input("Filepath: ")
input = open(filename, 'r')

print ("File Contents:\n" + input.read())

hash = pbkdf2_sha256.hash(input.read())

print("Hashing Result: \n" + hash)