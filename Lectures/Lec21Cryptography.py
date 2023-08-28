
# Uppercase
# print(ord('A'))
# print(ord('Z'))

# Lowercase
# print(ord('a'))
# print(ord('z'))

# print(chr(65))

# Requirement: Get message from user, then ask the user for key, and encrypt message

message_to_encrypt = input('Enter a message to encrypt: ')

# ask the user for a key

key = int(input('Enter a key: '))
# key: a number

# Encode the message, traverse it and replace each character with its cipher.

encrypted_message = ''
for i in message_to_encrypt:
    initial_value = ord(i)
    initial_value += key
    if initial_value > ord('z'):
        initial_value -= 26
    encrypted_message += chr(initial_value)  # calls __iadd__() for strings, changes in place

print(encrypted_message)

# circle back to a from z, only concerned with capital letters

