import os

path = 'E:\\share it\\app'
print()

for obj in os.scandir(path):
    print(obj)

print(os.path.getsize('image.jpg'))