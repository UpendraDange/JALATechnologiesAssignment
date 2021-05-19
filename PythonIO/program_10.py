"""
10. Write a program to read data from excel

"""
import xlrd

f1 = ("file_example.xls")

wb = xlrd.open_workbook(f1)
sheet = wb.sheet_by_index(0)

for i in range(8):
    # For row 0 and column 0
    print(sheet.cell_value(1, i), end = " ")

