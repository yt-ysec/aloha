import os

path = './mnist_mini_1000/'
files = os.listdir(path)

num4files = [file for file in files if 'num4' in file]

for file in num4files:
	print(file)

numOfNum4Files = len(num4files)

print('num4 files: ', numOfNum4Files)
