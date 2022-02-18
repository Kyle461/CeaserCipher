class CeaserCipher:
    def __init__(self):
        self.letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        self.key = {}
        #cnt is short for count
        self.cnt = 0

    def generate_key(self, n):
        #c is short for character
        for c in self.letters:
            self.key[c] = self.letters[(self.cnt + n) % len(self.letters)]
            self.cnt += 1
        return self.key
    
    def encrypt(self, key, message):
        cipher = ""
        for c in message:
            if c in key:
                cipher += key[c]
            else:
                cipher += c
        return cipher
    
def get_decryption_key(key):
    dkey = {}
    for c in key:
        dkey[key[c]] = c
    return dkey

ceaser_cipher = CeaserCipher()
# this is us generating the key which means shifting the letters
# by 3 I could have chose 1-26 as is the method of ceaser's cipher
# back in the day
key = ceaser_cipher.generate_key(3)

# this is us printing the key which when you look at it will show you
# how the letters are shifted (by 3) with two line breaks
print(key, end='\n\n')

# this is the message to be encrypted 
message = "YOU ARE AWESOME"

# this is us encrypting the message (creating the cipher)
cipher = ceaser_cipher.encrypt(key, message)

# this is us printing the cipher with two line breaks
print(cipher,end='\n\n')

# this is us decrypting the message
dkey = get_decryption_key(key)
message = ceaser_cipher.encrypt(dkey, cipher)

#this is us printing the decrypted message with two line breaks
print(message, end='\n\n')

# this is us breaking the cipher
# right now I am learning that to be able to have security you need to
# have a publicly available algorithm and not a secret algorithm...
for i in range(26):
    dkey = ceaser_cipher.generate_key(i)
    message = ceaser_cipher.encrypt(dkey,cipher)
    print(message)
