import dropbox

print(dropbox.__file__)
print("spacer")
print(dropbox.__version__)

acstoken = 'ADD YOUR DROPBOX ACCESS TOKEN HERE'
dbx = dropbox.Dropbox(acstoken)

with open('uploadMe.txt') as fileobj:
	tobuploaded = fileobj.read()

dbx.files_upload(tobuploaded.encode('utf-8'), '/uploaded2DropBox.txt')
