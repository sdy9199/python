import xlrd
Workbook = xlrd.open_workbook('book1.xlsx')
Worksheet = Workbook.sheet_by_name('Sheet1')
a1 = Worksheet._cell_values
for row in a1:
    print(row)
