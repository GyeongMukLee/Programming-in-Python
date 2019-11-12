import tkinter as tk

## 전역 변수 선언 부분 ##
fnameList = ["jeju1.gif", "jeju2.gif", "jeju3.gif", "jeju4.gif", "jeju5.gif",
             "jeju6.gif", "jeju7.gif", "jeju8.gif", "jeju9.gif"]

photoList = [None] * 9
num = 0


## 함수 선언 부분 ##
def clickNext():
    global num
    num += 1
    if num > 8:
        num = 0
    photo = tk.PhotoImage(file="Chapter10/GIF/" + fnameList[num])
    pLabel.configure(image=photo)
    btnFilename.configure(text=fnameList[num])
    pLabel.image = photo


def clickPrev():
    global num
    num -= 1
    if num < 0:
        num = 8
    photo = tk.PhotoImage(file="Chapter10/GIF/" + fnameList[num])
    pLabel.configure(image=photo)
    btnFilename.configure(text=fnameList[num])
    pLabel.image = photo


# 메인 코드 부분
window = tk.Tk()
window.geometry("700x500")
window.title("사진 앨범 보기")

btnPrev = tk.Button(window, text="<< 이전", command=clickPrev)
btnFilename = tk.Button(window, text=fnameList[num])
btnNext = tk.Button(window, text="다음 >>", command=clickNext)

photo = tk.PhotoImage(file="Chapter10/GIF/" + fnameList[0])
pLabel = tk.Label(window, image=photo)

btnPrev.place(x=250, y=10)
btnFilename.place(x=400, y=10)
btnNext.place(x=550, y=10)
pLabel.place(x=15, y=50)

window.mainloop()
