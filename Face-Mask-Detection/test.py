import tkinter
import tkinter.ttk as ttk

count = 0

def repeat_func():
    global app
    global label
    global count
    
    count += 1
    label.config(text=str(count))
    
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
    #i=0
    for r in emolist_:
                # ツリービューの要素に追加
        id = tree.insert("","end",tags=i, values=r)
        tree.config(r, )
        if i & 1:
                # tagが奇数(レコードは偶数)の場合のみ、背景色の設定
            tree.tag_configure(i,background="#CCFFFF")
        i+=1
    app.after(1000, repeat_func)



app = tkinter.Tk()
app.geometry("300x200")
app.title("TWEET TIMELINE")
app.geometry("1200x1300")
style_ = ttk.Style()
style_.configure("Treeview.Heading", font=("Yu Mincho", 12),rowheight=50)
style_.configure("Treeview", font=("Arial", 20),rowheight=80)
tree = ttk.Treeview(app, height=16)
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
label = tkinter.Label(app, width=15, height=1, text="0", font=("", 50))
label.pack()
tree.pack()

app.after(1000, repeat_func)

app.mainloop()