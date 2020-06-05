import pathlib
import os
pathname = 'E:\\flask_tutorial\\ShareIt\\app\\static\\css'  
#url = urllib.pathname2url(pathname)

url =  pathlib.Path(pathname).as_posix()
print(url)#.replace('file:///',''))