import openpyxl

wb = openpyxl.load_workbook('aloha.xlsx')
ws = wb['Sheet']

for i in range(9):
	ws.cell(row=1, column=1+i).value = 'ALOHA!'

wb.save('aloha.xlsx')
