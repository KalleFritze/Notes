import os

path = r"C:\Users\User\Desktop\nvim\lua\custom\plugins"


files = os.listdir(path)
for file in files:
    print(file)
    filepath = os.path.join(path, file)
    os.rename(filepath, filepath[0: len(filepath)-12]+".lua")
