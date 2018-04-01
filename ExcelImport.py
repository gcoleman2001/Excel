import xlrd

workbook = xlrd.open_workbook('C:\\Users\\Admin\\Desktop\\TestExcelImport.xlsx')
worksheet = workbook.sheet_by_name('Sheet1')
print(worksheet.cell(0,0).value)
print(worksheet.cell(1,0).value)
print(worksheet.cell(2,0).value)