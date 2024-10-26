import glob
import os

path = r"C:\Users\User\desktop\aaron\aadrawingpa\referencepng\landscape\australia"
allimages = os.listdir(path)
smallimages = []
print(type(os.path.getsize(os.path.join(path, "MEL-1715.jpg"))))
for image in allimages:
    if os.path.getsize(os.path.join(path, image)) < 1000000:
        smallimages.append(image)

for image in smallimages:
    print(image)


# print(len(allimages))
# print(len(smallimages))
