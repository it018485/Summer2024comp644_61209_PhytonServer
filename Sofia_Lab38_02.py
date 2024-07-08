import openpyxl

# Load the file
MioWb = openpyxl.load_workbook('SofiaExcelFile.xlsx')

# Select my sheet
MioSheet = MioWb["SofiaTab"]
# I read my cells
MioNome = MioSheet['A1'].value
MioNum = MioSheet['B1'].value
print("\n")
print(f"Cell A1 has my name: {MioNome}")
print(f"Cell B1 has the day I was born: {MioNum}","\n")
