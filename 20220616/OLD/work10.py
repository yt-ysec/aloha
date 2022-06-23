# ALOHA! を　9x9=81回書く
import openpyxl

wb = openpyxl.load_workbook('aloha.xlsx')
ws = wb['Sheet']

for j in range(9):
	for i in range(9):
		ws.cell(row=1+j, column=1+i).value = 'ALOHA!'


wb.save('aloha.xlsx')
