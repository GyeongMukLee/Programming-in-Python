import tkinter as tk


## 함수 선언 부분 ##
def FahToCel(fah: float) -> float:
    """
    화씨를 섭씨로 변환하는 함수
    """
    return (fah - 32) * (5 / 9)


def CelToFah(cel: float) -> float:
    """
    섭씨를 화씨로 바꾸는 함수
    """
    return cel * 9/5 + 32


def printResult() -> None:
    input_val = float(E1.get())
    if work.get() == 1:
        print("화씨를 섭씨로")
        return_val = FahToCel(input_val)
    elif work.get() == 2:
        print("섭씨를 화씨로")
        return_val = CelToFah(input_val)
    L2.configure(text=str(return_val))
    L2.pack(anchor="w")


## 메인 코드 부분 ##
window = tk.Tk()
window.title("섭씨 화씨 변환기")
work = tk.IntVar(window, 0)

R1 = tk.Radiobutton(window, text="화씨를 섭씨로", variable=work, value=1)
R2 = tk.Radiobutton(window, text="섭씨를 화씨로", variable=work, value=2)

R1.pack(anchor="w")
R2.pack(anchor="w")

L1 = tk.Label(window, text="입력: ")
L1.pack(side="left")

E1 = tk.Entry(window, bd=5)
E1.pack(side="left")

B1 = tk.Button(window, text="변환", command=printResult)
B1.pack(side="left")

L2 = tk.Label(window, text="")

window.mainloop()
