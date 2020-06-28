'''
import zipfile as z

with z.ZipFile('folder.zip','w') as zip_file:
    zip_file.write('test.py')
    zip_file.write('urlex.py')


'''

import random,string
import secrets
random_num = secrets.token_urlsafe(32)
print(random_num)