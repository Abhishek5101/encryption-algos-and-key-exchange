"""
convert message to Unicode
another random key with the same no of elements
create another list from their XOR result
To obtain the message back, take the resulted
list and XOR it with the random key list,
we'll get the message list back. Convert back to
alphabets
"""
import random


def encrypt():
    message = input("Enter message to be encoded\n")
    message_to_int = [ord(c) for c in message]

    random_key = []
    for i in range(len(message_to_int)):
        random_key.append(random.randint(1, 45))

    xor_operation = []

    for i in range(len(message_to_int)):
        xor_operation.append(message_to_int[i] ^ random_key[i])
        i += 1

    return xor_operation, random_key


def decrypt(xored_message, key):
    get_message_int_back = []

    for i in range(len(xored_message)):
        get_message_int_back.append(xored_message[i] ^ key[i])
        i += 1

    message_back = []

    for i in get_message_int_back:
        message_back.append(chr(i))
        i += 1

    message_back_string = ''.join(message_back)
    return message_back_string


"""
Below is an implementation of Diffie-Hellman key exchange protocol.
This protocol is used to make sure that the keys required for decryption
are transfered safely over the network by using a combination of Public and Private keys
from both receiver and transmitter.
The reason why the math always works is detailed in Documentation
"""

prime_numbers = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]


def diffie_hellman():
    prime_one = random.choice(prime_numbers)
    prime_root = random.choice(prime_numbers)

    alice_secret_key = random.randint(1, 1000)
    bob_secret_key = random.randint(1, 1000)

    alice_public_key = (prime_one ** alice_secret_key) % prime_root
    bob_public_key = (prime_one ** bob_secret_key) % prime_root

    answer_one = (bob_public_key ** alice_secret_key) % prime_root
    answer_two = (alice_public_key ** bob_secret_key) % prime_root

    print("This is the key you will be using when sharing messages: ", answer_one, '& ', answer_two)
    return answer_one, answer_two


