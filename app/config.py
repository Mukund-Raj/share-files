from wmi import WMI

c=WMI()


def Getdrives():
    '''
    Get all drives of current computer \n
    DriveType 2 and 3
    '''
    drives=[]
    for drive in c.Win32_LogicalDisk():
        if drive.DriveType ==2 or drive.DriveType == 3:
            drives.append(drive.Caption)
    return drives