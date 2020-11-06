from cryptography.fernet import Fernet
"""
Fernet guarantees that a message encrypted using it cannot be manipulated or read without the key. Fernet is an
implementation of symmetric (also known as “secret key”) authenticated cryptography. 

Fernet is built on top of a number of standard cryptographic primitives. Specifically it uses:
• AES (The Advanced Encryption Standard) in CBC mode with a 128-bit key for encryption; using PKCS7 padding.
• HMAC using SHA256 for authentication.
• Initialization vectors are generated using os.urandom().
"""
from random import choice
from string import ascii_lowercase, ascii_uppercase

def ncryptFunc(astring):
	encKey = Fernet.generate_key() # Generates a URL-safe base64-encoded 32-byte key that must be kept secret.
	print  ("Our key is: " + encKey.decode('utf-8') + '\n')
	f = Fernet(encKey)
	encryptedStr = f.encrypt(astring.encode('utf-8'))
	l = str(len(encKey))
	lengthList = []
	for _ in l:
		lengthList.append(_)
	randomStr1 = ''.join(choice(ascii_lowercase+ascii_uppercase) for i in range(9))
	randomStr2 = ''.join(choice(ascii_lowercase+ascii_uppercase) for i in range(9))
	print (str(astring) + ' \n after encryption: \n')
	print (randomStr1 + lengthList[0] + randomStr2 + lengthList[1]+ 
		(encKey).decode('utf-8').strip('=') + (encryptedStr).decode('utf-8'))

toBncryptd = "{'xmppsender': 'arman@xmpp.is', 'xmpppass': 'F#ckxmpp69!', 'xmpprecipient': 'init6@jabb3r.org'}"


ncryptFunc(toBncryptd)

"""
1. encrypts the string
2. determines the length of the key
3. inserts the digits of the lengths in a random string
4. creates a unified string from all strings

"""
