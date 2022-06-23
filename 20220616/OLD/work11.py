import os
from PIL import Image
import numpy as np
import openpyxl

path = './mnist_mini_1000/'
files = os.listdir(path)

wb = openpyxl.load_workbook('aloha.xlsx')
ws = wb['Sheet']

for file in files:
	if 'num4' in file:
		img = Image.open(path+file)
		imgArray = np.array(img)

		for i in range(9):
			for j in range(9):
				ws.cell(row=1+i, column=1+j).value = imgArray[i][j]

wb.save('aloha.xlsx')
