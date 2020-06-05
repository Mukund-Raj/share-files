import os
import posixpath

def return_image(path):
    pass



path=os.path.normpath('E:\\1 Shared files\\')
if os.path.exists(path):
    print('apth exists')

allpath = os.walk(path)

for p in allpath: 
    dirname,subdir,files = p
    #print(p)
    for file in files:
        filename = os.path.join(dirname,file)
        if os.path.isfile(filename):
            if os.path.getsize(filename) > 51200:
                ext=posixpath.splitext(filename)[1]
                if ext in ['.png','.jpeg','.jpg']:
                    #print("image file")
                    print(filename, ' is a image ', 'is of ',int(os.path.getsize(filename))/1024,' KB')
        #print('yes a file ')

'''
for file in os.listdir(path):
    #print(file)
    
    #print(file)
   
'''