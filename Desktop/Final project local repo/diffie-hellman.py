import random

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

    print(answer_two, answer_one)
    return answer_one, answer_two
