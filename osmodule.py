import os
import urllib
import html
import posixpath
import mimetypes
from colorama import init,Fore
#from termcolor import colored

mimetypes.init()
c="C:\\"
f="F:\\"

#print(alllfiles)

count_videos=0

print()
'''
for root,dirs,files in os.walk('C:\\',topdown=True) :
    for name in files:
        path=os.path.join(root,name)

        base,ext=posixpath.splitext(path)

        if ext in ['.mp4']:
            count_videos=count_videos + 1
'''         

for root,dirs,files in os.walk('E:\\',topdown=True) :
    for name in files:
        path=os.path.join(root,name)

        base,ext=posixpath.splitext(path)

        if ext in ['.mp4']:
            print()
            count_videos=count_videos + 1
            
'''
for root,dirs,files in os.walk('F:\\',topdown=True) :
    for name in files:
        path=os.path.join(root,name)

        base,ext=posixpath.splitext(path)

        if ext in ['.mp4']:
            count_videos=count_videos + 1
        
'''

print(count_videos)

    #print(dirs)


'''

path="E:\Fl1pp3d-2010-1080p-hdp0pc0rns.mp4"

f=open(path,'rb')


fs=os.fstat(f.fileno())

print(path.split('\\')[-1])


if os.path.isfile(path):
    print("flipped is a file")
    base,ext=posixpath.splitext(path)
    if ext in mimetypes.types_map:
        print(mimetypes.types_map[ext])



name='500 Days Of Summer (2009)'
url=urllib.parse.quote(name,errors='surrogatepass')
print(url)

file="E:\Ball in  a cup-32Bit\Ball in a cup.exe"
if os.path.isfile(file):
        print(f"{file} is a  file")

path=r"E:\\flask_tutorial\\C3S\\app"

dir=os.listdir("E:\\")

print(type(dir))

list_dir = ('\n').join(dir)

init()

print(Fore.BLUE + 'some red text')

#print(colored('hello world'))

#print("\033[1;37;40m Bright Colour\033")
'''
'''
for file in dir:
    if os.path.isfile(os.path.join("E:\\",file)):
        print(f"{file} is a  file")

    if os.path.isdir(os.path.join("E:\\",file)):
        print(f"{file} is an another folder")
'''
#print(list_dir)




#print(os.path.abspath(path))