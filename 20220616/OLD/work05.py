# 'num4' ファイルが何個あるか？　カウントして表示する
import os

path = './mnist_mini_1000/'
files = os.listdir(path)

numOfNum4Files = 0

for file in files:
	if 'num4' in file:
		print(file)
		numOfNum4Files = numOfNum4Files + 1

print('num4 files: ', numOfNum4Files)
