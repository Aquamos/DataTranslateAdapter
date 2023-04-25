from test import get_manga_name
from xlsxToDataframe import convertExcelToDataframe

filepath = 'DanyloMangalib.xlsx'
sheet_name = 'Data'
mangas_df = convertExcelToDataframe(filepath, sheet_name)

with open("file.txt", "a") as f:
    for e in mangas_df['Название']:
        res = get_manga_name(e)
        print(res)
        f.write(f"{res}\n")
