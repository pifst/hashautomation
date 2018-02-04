from passlib.hash import pbkdf2_sha256
#import sys
from contextlib import redirect_stdout




filename = input("Filepath: ")
input = open(filename, 'r')

#print ("File Contents:\n" + input.read())

hash = pbkdf2_sha256.hash(input.read())

#print("Hashing Result: \n" + hash)
#sys.stdout = open('hashoutput.txt', 'w')

with open('hashoutput.txt', 'w') as f:
    with redirect_stdout(f):
    	print ("File Contents:\n" + input.read())
        #print ("Hashing Result: \n" + hash)