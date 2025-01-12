import tkinter as tk
from tkinter import filedialog, messagebox

import tranceporter as tp

selected_folder_before_path = ""
selected_folder_after_path = ""

def select_folder_before():
    folder_path = filedialog.askdirectory()  # フォルダ選択ダイアログを表示
    if folder_path:  # フォルダが選択された場合
        selected_folder_before_path = folder_path
        folder_label_before.config(text=f"変更元 : {folder_path}")
    else:  # キャンセルされた場合
        messagebox.showwarning("キャンセル", "フォルダが選択されませんでした。")

def select_folder_after():
    folder_path = filedialog.askdirectory()  # フォルダ選択ダイアログを表示
    if folder_path:  # フォルダが選択された場合
        selected_folder_after_path = folder_path
        folder_label_after.config(text=f"変更後 : {folder_path}")
    else:  # キャンセルされた場合
        messagebox.showwarning("キャンセル", "フォルダが選択されませんでした。")

def convert_data():
    if select_folder_before == '':
        messagebox.showwarning("キャンセル", "フォルダが選択されません。")
    else:
        
        print(selected_folder_before_path)
        #tp.convert_xls_to_xlsx(select_folder_before_path)
        messagebox.showwarning("変換完了", "変換が終了しました")
    

# メインウィンドウの作成
root = tk.Tk()
root.title("xls to xlsm converter")
root.geometry("400x200")  # ウィンドウサイズ


# ウィンドウのサイズを固定
root.resizable(False, False)

# ボタンの作成
folder_button_frame = tk.Frame(root)
folder_button_frame.pack(pady=20)
button_before = tk.Button(folder_button_frame, text="変更元のフォルダを選択", command=select_folder_before)
button_before.pack(side=tk.LEFT, padx=5)
button_after = tk.Button(folder_button_frame, text="変更後のフォルダを選択", command=select_folder_after)
button_after.pack(side=tk.RIGHT, padx=5)

folder_label_before = tk.Label(root,text="変更元 : フォルダが選択されていません",wraplength=350)
folder_label_before.pack(pady=(10,0))
folder_label_after = tk.Label(root,text="変更後 : フォルダが選択されていません",wraplength=350)
folder_label_after.pack()
#------------------------------------

another_button = tk.Button(text="変換",command=convert_data)
another_button.pack(pady=20)  # 左に配置

#------------------------------------
# メインループの開始
root.mainloop()