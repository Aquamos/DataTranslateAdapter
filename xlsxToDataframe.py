import pandas as pd

def convertExcelToDataframe(filepath, sheet_name):
    excel_file = pd.ExcelFile(filepath)
    return pd.read_excel(excel_file, sheet_name)
