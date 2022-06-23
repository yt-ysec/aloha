import os
import numpy as np
from PIL import Image
import openpyxl

path = './mnist_mini_1000/'
files = os.listdir(path)

wb = openpyxl.Workbook()
ws = wb['Sheet']

for file in files:
	if 'num4' in file:
		print(file)
		img = Image.open(path+file)
		imgArray = np.array(img)
		ws.cell(row=1+i, column=1+j).value = imgArray[i][j]

wb.save('test.xlsx')
