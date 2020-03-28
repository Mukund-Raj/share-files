from wmi import WMI

c=WMI()

drives=[]


for drive in c.Win32_LogicalDisk ():
    drives.append(drive.Caption[0])