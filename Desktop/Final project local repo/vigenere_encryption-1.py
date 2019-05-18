"""
In this project, I've prirotized creating own functions
rather than using libraries and other tools whenever seemed possible.
Hence you might find this code needlessly long.
Detailed explanation is provided in the documentation
"""

import string


dictionary = dict(zip(string.ascii_lowercase, range(1, 27)))

# Since in python, dictionaries are mapped one way and there is no built in function
# to get a key back from a value, we write a function just for that


def letter(number):
    for k, v in dictionary.items():
        if number == v:
            return k


def clean_up_message():
    my_string = input("Enter my_string message")
    my_string = my_string.replace(' ', '').lower()
    return my_string


keyword = input("enter short string keyword\n")
key_index = 0
key = ""
message = clean_up_message()
for i in message:
    key += keyword[key_index % len(keyword)]
    key_index += 1

    if key_index >= len(key):
        key_index %= len(key)


message_numbers = [dictionary[letter] for letter in message]
key_numbers = [dictionary[letter] for letter in key]


addition_list = []
for i in range(len(message_numbers)):
    addition_list.append((message_numbers[i] + key_numbers[i]) % 26)
    i += 1


subtraction_list = []
for i in range(len(addition_list)):
    subtraction_list.append((addition_list[i] - key_numbers[i]) % 26)
    i += 1


def encrypt(list_of_numbers):
    for j in list_of_numbers:
        print(letter(j), end=" ")
    print("\n")


def decrypt(encoded_list):
    for number in encoded_list:
        print(letter(number), end="")


encrypt(addition_list)
decrypt(subtraction_list)

# This program doesnt account for punctuations
