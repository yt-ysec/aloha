import os
from PIL import Image
import numpy as np
import openpyxl

path = './mnist_mini_1000/'
files = os.listdir(path)

wb = openpyxl.load_workbook('aloha.xlsx')
ws = wb['Sheet']

numOfNum4Files = 0

for file in files:
	if 'num4' in file:
		print(file)
		img = Image.open(path+file)
		imgArray = np.array(img)

		for i in range(9):
			for j in range(9):
				ws.cell(row=1+i, column=1+j+9*numOfNum4Files).value = imgArray[i][j]
		numOfNum4Files = numOfNum4Files + 1

wb.save('aloha.xlsx')
