import os
import xlwings as xw

def convert_xls_to_xlsx(directory1, directory2):
    # 保存先ディレクトリが存在しない場合は作成
    if not os.path.exists(directory2):
        os.makedirs(directory2)

    for filename in os.listdir(directory1):
        if filename.endswith('.xls'):
            xls_file = os.path.join(directory1, filename)
            xlsx_file = os.path.join(directory2, filename.replace('.xls', '.xlsx'))
            
            # Excelアプリケーションを起動
            app = xw.App(visible=False)
            try:
                # .xlsファイルを開く
                wb = app.books.open(xls_file)
                # .xlsx形式で保存
                wb.save(xlsx_file)
                print(f'Converted: {filename} to {os.path.basename(xlsx_file)}')
            except Exception as e:
                print(f"Error converting {filename}: {e}")
            finally:
                # Excelアプリケーションを終了
                try:
                    wb.close()
                except:
                    pass
                app.quit()