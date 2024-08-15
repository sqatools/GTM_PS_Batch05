import openpyxl
"""
pip install openpyxl
"""


def read_content_from_excel(filename, sheet_name, cell_name):
    wb = openpyxl.load_workbook(filename)
    sheet = wb[sheet_name]
    cell = sheet[cell_name]
    print(cell.value)


#read_content_from_excel("test_excel_data.xlsx", sheet_name="Sheet1", cell_name="A2")
#read_content_from_excel("test_excel_data.xlsx", sheet_name="Sheet1", cell_name="A3")
#read_content_from_excel("test_excel_data.xlsx", sheet_name="Automation", cell_name="A2")


#for i in range(1, 5):
#   read_content_from_excel("test_excel_data.xlsx", sheet_name="Automation", cell_name=f"A{i}")

"""
Python
Selenium
Pytest
API Testing
"""


def read_all_rows_content_from_excel(filename, sheet_name):
    wb = openpyxl.load_workbook(filename)
    sheet = wb[sheet_name]
    max_row = sheet.max_row
    print(max_row)
    max_col = sheet.max_column
    print(max_col)
    cell_val = sheet.cell(1, 1).value
    print(cell_val)

    for row in range(1, max_row+1):
        for col in range(1, max_col+1):
            print(sheet.cell(row, col).value, end=" ")
        print()




read_all_rows_content_from_excel("test_excel_data.xlsx", "Sheet2")
