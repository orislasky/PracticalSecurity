import requests

def uploaderFunc(filePath):

	with open(filePath, 'r') as file0bj:
		myString = file0bj.read()

	req = requests.post('https://file.io', data={"text":myString})
	print (req.json())
	print (req.json()['link'])
	return req.json()['link']

uploaderFunc('uploadMe.txt')
