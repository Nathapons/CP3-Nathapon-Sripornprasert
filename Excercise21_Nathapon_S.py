from tkinter import *
import math

def calculate_bmi(event):
    bmi = float(text_box_weight.get()) / math.pow(float(text_box_height.get())/100,2)
    if bmi > 30.0:
        grade = "อ้วนมาก"
    elif bmi > 25.0:
        grade = "อ้วน"
    elif bmi > 23.0:
        grade = "น้ำหนักเกิน"
    elif bmi > 18.6:
        grade = "น้ำหนักปกติเหมาะสม"
    else:
        grade = "ผอมเกินไป"
    result.configure(text = grade)

main = Tk()
label_height = Label(main, text="ส่วนสูง (cm)",font=('Consalas',14)).grid(row=0, column=0)
text_box_height = Entry(main)
text_box_height.grid(row=0, column=1)
label_weight = Label(main, text="น้ำหนัก (kg)",font=('Consalas',14)).grid(row=1, column=0)
text_box_weight= Entry(main)
text_box_weight.grid(row=1, column=1)
CalculateButton = Button(main,text="คำนวณ")
CalculateButton.grid(row=2,column=0)
result = Label(main, text="ผลลัพธ์",font=('Consalas',14))
result.grid(row=2, column=1)
CalculateButton.bind('<Button-1>',calculate_bmi)
main.mainloop()