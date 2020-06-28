import shutil
import os

zip=shutil.make_archive('app','zip','E:\\share it\\app')
path = 'E:\\share it\\app\\app1\\app2'
print(zip)
print(os.path.split(path))
import time

time.sleep(3)

os.remove(zip)
