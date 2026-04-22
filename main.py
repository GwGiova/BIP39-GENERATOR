#Library to create a secure 2^n bits number
import secrets

import hashlib

import words

def calculateChecksum(NB, ENT):

    #I calculate the n of bits that the checksum must have
    #Doing ENT (Entropy) / 32
    BitsToTake = int(ENT/32)

    #I calculate the Sha256's Hash of the Number
    Sha256Hash = hashlib.sha256(NB).hexdigest()

    #I convert from the HEX format to INT
    Sha256HashINTformat = int(Sha256Hash, 16)

    #I convert from the INT format to STR
    #I use [2:] to remove the initial '0b' added by the bin() function
    Sha256StringBINformat = bin(Sha256HashINTformat)[2:].zfill(256)

    #Calculate the CSUM
    checksum = Sha256StringBINformat[:BitsToTake]

    return checksum

def printWords(FS):

    #Creating a counter to keep track of the number of phrases printed
    counter = 0

    while counter + 11 <= len(FS):

        #I fetch groups of 11 bits from the final string, with an offset of 11 bits every time a phrases is fetched
        groupOf11Bits = FS[counter:counter+11]
        
        #I print the phrase fetched from the dictionary (In the words.py file)
        print(words.BIP39[groupOf11Bits])
        
        #I increment the counter
        counter += 11




#START OF THE PROGRAM

#I ASK WHETHER THE USER WANTS TO GENERATE AN ENTROPY OF 128 OR 256 BIT, FOR THE NUMBER WE WILL GENERATE
entropy = int(input("Insert the entropy that your number will have (128 or 256): "))

#CHECK USER INPUT
while entropy != 128 and entropy != 256:

    entropy = int(input("Insert the entropy that your number will have (128 or 256): "))

#I GENERATE THE 128 / 256 BIT NUMBER (INT)
number = secrets.randbits(entropy)

#Convert the Number from INT to BYTES
numberBYTESformat = number.to_bytes(entropy, "big")

checksum = calculateChecksum(numberBYTESformat, entropy)

#I use [2:] to remove the initial '0b' added by the bin() function
numberStringBINformat = bin(number)[2:]

#The final string is the result of the number binary representation + checksum
finalString = numberStringBINformat + checksum

printWords(finalString)
