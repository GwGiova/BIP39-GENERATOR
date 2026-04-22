# BIP39 STANDARD
This program follows the BIP39 standard for the creation of seed phrases.  
The generated seed phrases serve as "a key" for a crypto wallet.  
The BIP39 standard is widely accepted by crypto wallets, such as Metamask and Phantom.

The program works as follows:

A 128 / 256 bit number is generated using the `secrets` library.  
Then we calculate the number's SHA256() using the `hashlib` library.  
The checksum is then calculated by taking the first ENTROPY/32 bits of the binary SHA256 hash.  
The checksum is then added at the end of the binary number representation.  
FinalString = number + checksum.  
Then the final string is divided into groups of 11 bits, resulting in 12 or 24 words (depending on the entropy).  
Every combination of 11 bits (2048) corresponds to a word in the BIP39 standard.  
Then we associate each group with its corresponding word.

# SUMMARY
ENT = 128 → 12‑word mnemonic  
ENT = 256 → 24‑word mnemonic  
Fully compliant with the BIP39 specification  
Uses cryptographically secure randomness (`secrets`)  
Compatible with major crypto wallets  
