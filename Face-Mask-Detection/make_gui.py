# tkinterのインポート
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText
import tkinter.font
from mlask import MLAsk
import wave
from playsound import playsound
import datetime

# 関数birthdayの定義
def birthday():
    word = entry.get("1.0", "end-1c")
    try:
        emotion = list(MLAsk().analyze(word).get('emotion').keys())[0]
    except AttributeError:
        emotion = 'nor'
    dt_now = datetime.datetime.now()
    date = dt_now.strftime('%Y年%m月%d日 %H:%M:%S')
    datalist = [emotion, word, date]
    print("datalist=", datalist)
    with open('emolist.txt', 'a') as f:
        f.writelines("%s\n" % datalist)
    f.close
    f = open('emolist.txt', 'r')
    emodata = f.read().splitlines()
    f.close()
    data_len = len(emodata)
    emotion = emodata[data_len-1][2:5]
    if (emotion == 'awa'):
        playsound('voice/awa.wav')
        playsound('voice/awa.wav')
    elif (emotion == 'yor'):
        playsound('voice/yor.wav')
        playsound('voice/yor.wav')
    elif (emotion == 'ika'):
        playsound('voice/ika.wav')
        playsound('voice/ika.wav')
    elif (emotion == 'kow'):
        playsound('voice/kow.wav')
        playsound('voice/kow.wav')
    elif (emotion == 'haj'):
        playsound('voice/haj.wav')
        playsound('voice/haj.wav')
    elif (emotion == 'suk'):
        playsound('voice/suk.wav')
        playsound('voice/suk.wav')
    elif (emotion == 'iya'):
        playsound('voice/iya.wav')
        playsound('voice/iya.wav')
    elif (emotion == 'tak'):
        playsound('voice/tak.wav')
        playsound('voice/tak.wav')
    elif (emotion == 'yas'):
        playsound('voice/yas.wav')
        playsound('voice/yas.wav')
    elif (emotion == 'odo'):
        playsound('voice/odo.wav')
        playsound('voice/odo.wav')
    elif (emotion == 'nor'):
        playsound('voice/nor.wav')
        playsound('voice/nor.wav')

    messagebox.showinfo("ツイート","あなたのツイートは" + word + "です")
    entry.delete(0,tk.END)
    return emotion

# rootフレームの設定
root = tk.Tk()
root.title("ツイート")
root.geometry("1820x1000")
font = tkinter.font.Font(root, size=50)
# フレームの作成と設置
frame = ttk.Frame(root)
frame.grid(column=0, row=0, sticky=tk.NSEW, padx=200, pady=300)
#style = ttk.Style()
#style.configure("office.TButton", font=50, anchor="w")
# 各種ウィジェットの作成
label = ttk.Label(frame, text="いまどんな気持ち？", font=tkinter.font.Font(root, size=30))
#entry = ttk.Entry(frame, width=30, font=("", 30))
entry = ScrolledText(frame, width=100, font=("", 15))
entry.grid(column=0, row=0, padx=100, pady=1, ipadx=10, ipady=1)
#entry.place(x=20, y=20, width=50, height=5000)

button_execute = tk.Button(frame, width=20, height=10,text="ツイートする", command=birthday)
button_execute.place(x=200, y=200, width=1500, height=300)
#button_execute = ttk.Button(frame, text="ツイートする")
# 各種ウィジェットの設置
label.grid(row=0, column=0)
entry.grid(row=0, column=1)
button_execute.grid(row=1, column=1)
#win = tk.Toplevel(root)
root.attributes("-topmost", True)
root.mainloop()

'''
emotion_analyzer = MLAsk()
word = entry.get()
just_analyze = emotion_analyzer.analyze(word)
emotion_key = emotion_analyzer.analyze(word).get('emotion').keys()

print(just_analyze)
print(list(emotion_key)[0]=='iya')
'''