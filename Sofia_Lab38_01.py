from openpyxl import Workbook

# nuovo workbook and I add a Sheet with a personalized name
MioWb = Workbook()
MioSheet = MioWb.active
MioSheet.title = "SofiaTab"

# Add my values
MioSheet['A1'] = 'Sofia'
MioSheet['B1'] = 27

# Save the workbook file
MioWb.save('SofiaExcelFile.xlsx')



