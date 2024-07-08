import openpyxl

# Load the file
MioWb = openpyxl.load_workbook('SofiaExcelFile.xlsx')

# Select my sheet
MioSheet = MioWb["SofiaTab"]
# Change my name  in A1
MioSheet['A1'] = "Alice"
MioNome = MioSheet['A1'].value
MioWb.save("SofiaExcelFile.xlsx")

print("\n")
print(f"Cell A1 has my NEW name: {MioNome}","\n")
