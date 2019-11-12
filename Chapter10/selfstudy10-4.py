import tkinter as tk
import tkinter.messagebox


## 함수 선언 부분 ##
def keyEvent(event):
    tk.messagebox.showinfo(
        title="키보드 이벤트", message="눌린 키: "+chr(event.keycode))


def keyEventShift(event):
    tk.messagebox.showinfo


## 메인 코드 부분 ##
window = tk.Tk()

window.bind("<Key>", keyEvent)

window.bind("<Shift-Up>",
            lambda event: tk.messagebox.showinfo(title="키보드 이벤트", message="눌린 키: Shift + 위쪽 화살표"))
window.bind("<Shift-Down>",
            lambda event: tk.messagebox.showinfo(title="키보드 이벤트", message="눌린 키: Shift + 아래쪽 화살표"))
window.bind("<Shift-Left>",
            lambda event: tk.messagebox.showinfo(title="키보드 이벤트", message="눌린 키: Shift + 왼쪽 화살표"))
window.bind("<Shift-Right>",
            lambda event: tk.messagebox.showinfo(title="키보드 이벤트", message="눌린 키: Shift + 오른쪽 화살표"))


window.mainloop()
