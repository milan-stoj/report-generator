import xlsxwriter
import os
def csvGen(self):
    tests = []
    for index in range(self.listWidget.count()):
        tests.append(self.listWidget.item(index).text())
    

# Create a workbook and add a worksheet.
    workbook = xlsxwriter.Workbook('tests.xlsx')
    worksheet = workbook.add_worksheet()
    
    # Some data we want to write to the worksheet.
    bold = workbook.add_format({'bold': True})
    worksheet.write('A1', 'Recommended Testing', bold)
    # Start from the first cell. Rows and columns are zero indexed.
    row = 1
    col = 0
    
    # Iterate over the data and write it out row by row.
    for i in tests:
        worksheet.write(row, col,     i)
        row += 1
    
    workbook.close()
    os.startfile("tests.xlsx")
    