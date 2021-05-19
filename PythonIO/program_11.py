"""
11. Write a program to write data to excel
"""

import xlsxwriter

objWorkbook = xlsxwriter.Workbook("file_example2.xlsx")
objSheet = objWorkbook.add_worksheet()

names = ["Sachin", "Virat", "Rohit"]
values = [70, 30, 100]

objSheet.write("A1", "Names")
objSheet.write("B1", "Scores")

for i in range(len(names)):
    objSheet.write(i+1, 0, names[i])
    objSheet.write(i+1, 1, values[i])

objSheet.write("E1", "Total")
objSheet.write_formula("E2","=SUM(B2:B4)")

objWorkbook.close()
