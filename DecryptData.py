from cryptography.fernet import Fernet
from ast import literal_eval

def dcryptFunc(strng):
	lengthString = strng[:20]
	lengthList=[]
	for i in lengthString:
		if i.isdigit():
			lengthList.append(i)
	
	l = int(lengthList[0]+lengthList[1])
	decKey= strng[20:19+l] + chr(61) # chr(61) is '='
	f = Fernet(decKey)
	tobDecrypted = strng[19+l:]
	decryptedString = f.decrypt(tobDecrypted.encode('utf-8'))
	final_decrptd= literal_eval(decryptedString.decode('utf-8'))
	print ("Our Encrypted string is now of type : " )
	print (type(final_decrptd))
	print ("... And here's the decrypted string: ")
	return final_decrptd 

s = 'OWfhsEXaC4ClIQnxOVJ4Zji_0fOojJpnnfDGlZEnbXGrNFJmyIlKY6bd7D6B5r0gAAAAABcAd9mHCBclZ-TiRYp09AGfVViRHZLJ2utfB8PiLWRUtJYJCFjGkwKrOAusac5wzDHnd0OYXkThQqlM8UMD6IoHHPInMTu7I_rp8Obx94j-HTo2yJ7BYKbfTVigeKtk7kIsqMFxx4Cw7n8VUbRrO7ew6jUWA=='
print (dcryptFunc(s))