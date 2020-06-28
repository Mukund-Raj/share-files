import zipfile as z

with z.ZipFile('folder.zip','w') as zip_file:
    zip_file.write('test.py')
    zip_file.write('urlex.py')