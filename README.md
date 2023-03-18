# Passphrase_generator_BIP39

This Python script generates random passphrases using BIP39 wordlists. Passphrases can be used to generate cryptographic keys, as a more user-friendly alternative to using complex passwords.

## Requirements
-Python 3
-BIP39 wordlist file in plain text format (English wordlist provided by default)
## Installation
Download the script and save it in a local directory.
Place the BIP39 wordlist file in the same directory with the script.
Open a terminal window and navigate to the directory where the script is saved.
Run the script by typing python3 passphrase_generator.py and pressing Enter.
### Usage
The script will prompt the user to input the number of passphrases they want to generate.
The script will generate the specified number of passphrases, with each passphrase consisting of 12 random words.
The passphrases will be saved to a file named passphrases.txt in the same directory with the script.
The script will print the generated passphrases to the console.
Note: The number of words in each passphrase can be adjusted by changing the parameter passed to the generate_mnemonic() function.
