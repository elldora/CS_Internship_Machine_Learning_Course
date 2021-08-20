import zipfile
with zipfile.ZipFile('C:\\Users\\Green\\CS_Internship_ML\\Step_04\\HISTDATA_COM_XLSX_EURUSD_M12018.zip', 'r') as zip_ref:
    zip_ref.extractall('C:\\Users\\Green\\CS_Internship_ML\\Step_04\\Unzipped_EURUSD_File')


import os, os.path
file_names = os.listdir('C:\\Users\\Green\\CS_Internship_ML\\Step_04\\Unzipped_EURUSD_File')
for i in range (len(file_names)):
    print(file_names[i])

# with open('C:\\Users\\Green\\CS_Internship_ML\\Step_04\\Unzipped_EURUSD_File\\'+file_names[0]) as f:
#     print(f.readlines())

# import openpyxl
# from pathlib import Path

# xlsx_file = Path('Unzipped_EURUSD_File', 'HISTDATA_COM_XLSX_EURUSD_M12018.xlsx')
# wb_obj = openpyxl.load_workbook(xlsx_file) 

# # Read the active sheet:
# sheet = wb_obj.active
