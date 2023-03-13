""" 
password generator
generates 8 digit password with:
- 2 uppercase letters
- 2 lowercase letters
- 2 digits from 0 - 9
- 2 punctuations such as "!, ? #, $
"""
import random

# Generating all characters
uppercase1 = chr(random.randint(65, 90))
uppercase2 = chr(random.randint(65, 90))

lowercase1 = chr(random.randint(97, 122))
lowercase2 = chr(random.randint(97, 122))

digit1 = chr(random.randint(48, 57))
digit2 = chr(random.randint(48, 57))

punc1 = chr(random.randint(33, 38))
punc2 = chr(random.randint(33, 38))

# Adding all characters into one 8 digit password. 
password = uppercase1 + uppercase2 + lowercase1 + lowercase2 + digit1 + digit2 + punc1 + punc2

# randomize digits
def randomize(password):
    p = random.sample(password, len(password))
    return ''.join(p)

# print final password
final_pass = randomize(password)
print(final_pass)