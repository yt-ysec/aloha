# Excelファイルに ALOHA! と書く練習
import openpyxl

wb = openpyxl.Workbook()
ws = wb['Sheet']
ws.cell(row=1, column=1).value = 'ALOHA!'
wb.save('aloha.xlsx')
