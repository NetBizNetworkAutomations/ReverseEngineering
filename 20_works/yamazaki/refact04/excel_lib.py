from openpyxl import load_workbook

def open_workbook(filename):
    wb = load_workbook(filename)
    return wb

def save_excel(wb, filename):
    wb.save(filename)
