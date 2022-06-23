# ファイル名に 'num4' があるときだけ、表示する
import os

path = './mnist_mini_1000/'
files = os.listdir(path)

for file in files:
	if 'num4' in file:
		print(file)

