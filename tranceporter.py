import pandas as pd # type: ignore
import os

def convert_xls_to_xlsx(directory1,directory2):
    for filename in os.listdir(directory1):
        if filename.endswith('.xls'):
            xls_file = os.path.join(directory1, filename)
            xlsx_file = os.path.join(directory2, filename.replace('.xls', '.xlsx'))
            
            # .xlsを読み込んで、.xlsxとして保存
            df = pd.read_excel(xls_file, engine='xlrd')
            df.to_excel(xlsx_file, index=False, engine='openpyxl')
            print(f'Converted: {filename} to {filename.replace(".xls", ".xlsx")}')
