# Tkinterのライブラリを取り込む
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
import os


# ファイルの参照処理
def click_refer_button():
    fTyp = [("","*")]
    iDir = os.path.abspath(os.path.dirname(__file__))
    filepath = '/home/buffalo/ansugaaa/Face-Mask-Detection/emolist.txt'
    file_path.set(filepath)


# 出力処理
def click_export_button():
    path = file_path.get()
    if path[-4:] == '.txt':
        f = open(path, encoding="utf-8")
        text_data = f.read()
        textBox.insert(END, text_data)

if __name__ == '__main__':
    # ウィンドウを作成
    root = tkinter.Tk()
    root.title("hello world") # アプリの名前
    root.geometry("500x500") # アプリの画面サイズ
    '''
    # Frame1の作成
    frame1 = ttk.Frame(root, padding=10)
    frame1.grid()

    # 「ファイル」ラベルの作成
    s = StringVar()
    s.set('ファイル名：')
    label1 = ttk.Label(frame1, textvariable=s)
    label1.grid(row=0, column=0)

    # 参照ファイルのパスを表示するテキストボックスの作成
    file_path = StringVar()
    filepath_entry = ttk.Entry(frame1, textvariable=file_path, width=50)
    filepath_entry.grid(row=0, column=1)

    # 参照ボタンの作成
    refer_button = ttk.Button(frame1, text=u'参照', command=click_refer_button)
    refer_button.grid(row=0, column=2)
    '''
    file_path = '/home/buffalo/ansugaaa/Face-Mask-Detection/emolist.txt'

    # Frame2の作成
    frame2 = ttk.Frame(root, padding=10)
    frame2.grid()

    # テキスト出力ボタンの作成
    export_button = ttk.Button(frame2, text='ファイルの中身を出力', command=click_export_button, width=20)
    export_button.grid(row=0, column=0)

    # テキスト出力ボックスの作成
    textboxname = StringVar()
    textboxname.set('\n\n出力内容 ')
    label3 = ttk.Label(frame2, textvariable=textboxname)
    label3.grid(row=1, column=0)
    textBox = Text(frame2, width=50)
    textBox.grid(row=2, column=0)

    # ウィンドウを動かす
    root.mainloop()