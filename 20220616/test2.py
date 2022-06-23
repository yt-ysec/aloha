import openpyxl

wb = openpyxl.Workbook()
ws = wb['Sheet']

for j in range(9):
	for i in range(9):
		ws.cell(row=1+j, column=1+i).value = 'HELLO!'

wb.save('test.xlsx')
