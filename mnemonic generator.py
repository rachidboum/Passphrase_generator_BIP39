import random

# Replace this with the path to your BIP39 wordlist file
WORDLIST_PATH = 'english.txt'

def generate_mnemonic(num_words):
    with open(WORDLIST_PATH, 'r') as f:
        wordlist = [line.strip() for line in f]
    indices = [random.randint(0, len(wordlist)-1) for _ in range(num_words)]
    return ' '.join([wordlist[i] for i in indices])

# Ask the user for the number of passphrases they want
num_passphrases = int(input("How many passphrases do you want to generate? "))

# Generate the passphrases and save them to a file
with open('passphrases.txt', 'w') as f:
    for i in range(num_passphrases):
        passphrase = generate_mnemonic(12)  # Change 12 to the desired number of words
        f.write(passphrase + '\n')
        print(f"Passphrase {i+1}: {passphrase}")

print(f"{num_passphrases} passphrases have been generated and saved to passphrases.txt")
