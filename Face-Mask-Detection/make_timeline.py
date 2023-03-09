import tkinter
from tkinter import font
# モジュールのインポート
import tkinter as tk
import tkinter.ttk as ttk
import time

root_ = tk.Tk()
root_.title("TWEET TIMELINE")
root_.geometry("1200x1300")

# ツリービューの作成
style_ = ttk.Style()
style_.configure("Treeview.Heading", font=("Yu Mincho", 12),rowheight=50)
style_.configure("Treeview", font=("Arial", 20),rowheight=80)
tree = ttk.Treeview(root_, height=16)
# 列インデックスの作成
tree["columns"] = (1,2,3)
# 表スタイルの設定(headingsはツリー形式ではない、通常の表形式)
tree["show"] = "headings"
# 各列の設定(インデックス,オプション(今回は幅を指定))
tree.column(1,width=150)
tree.column(2,width=600)
tree.column(3,width=350)
# 各列のヘッダー設定(インデックス,テキスト)
tree.heading(1,text="いまの気持ち")
tree.heading(2,text="Tweet")
tree.heading(3,text="日付")

def makeTimeline():    
        #print(len(emolist_))
    while True:    
        # ルートフレームの作成
        path = 'emolist.txt'
        emolist = []
        with open(path) as f:
            for s_line in f:
                #print(s_line)
                emolist.append(s_line)
        emolist_ = []
        num = 0
        for i in reversed(range(len(emolist))):
            num = num + 1
            emotion = '@'+emolist[i].split(',')[0][2:-1]
            tweet = emolist[i].split(',')[1][2:-1]
            datetime = emolist[i].split(',')[2][2:-3]
            emolist_.append(list([emotion, tweet, datetime]))
            if (num == 16):
                break
            
            
        i=0
            #print(emolist_)
        for r in emolist_:
                # ツリービューの要素に追加
            tree.insert("","end",tags=i, values=r)
            if i & 1:
                    # tagが奇数(レコードは偶数)の場合のみ、背景色の設定
                tree.tag_configure(i,background="#CCFFFF")
            i+=1
            # ツリービューの配置
        tree.pack()
        #root_.after(100, makeTimeline)
        root_.mainloop() 
        
            #root_.mainloop()

#root_.update()  # updateをコールして再帰的コールをキックする
while True:
    root_.mainloop
#root_.after(1, makeTimeline)
# 以後のイベント処理はmainloop内で実行される
    
    
