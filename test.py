from tkinter import *
from tkinter import messagebox as msgbox
from tkinter import filedialog as fd
import pandas as pd

class AncWindow(Tk):

    def __init__(self, parent):
        self.user_interface()

    def user_interface(self):
        # User interface
        main_window = Tk()
        main_window.geometry("500x250")
        main_window.title("Cross Section System")
        # Widget
        welcome_label = Label(main_window, text="Welcome to Cross Section System",
                              font=("Monospaced", 24), fg="white", bg="blue")
        name_and_tel_label = Label(main_window, text="Create by Nathapon.S Tel 4955", font=("Monospaced", 16))
        start_button = Button(main_window, text="Start Program", font=("Monospaced", 16),
                              command=self.select_product_gui,width=30, height=2)
        exit_button = Button(main_window, text="Exit Program", command=quit,
                             font=("Monospaced", 16), width=30, height=2)
        # Widget and GUI Place
        welcome_label.place(x=3, y=0)
        name_and_tel_label.place(x=100, y=60)
        start_button.place(x=60, y=100)
        exit_button.place(x=60, y=180)
        main_window.mainloop()

    def select_product_gui(self):
        information_message = msgbox.showinfo(title="Information",message="Please select product and version")
        #GUI
        main_window2 = Tk()
        main_window2.geometry("400x200")
        main_window2.title("Input Product and Lot")
        #Widget
        select_item_label = Label(main_window2,text="Select item and version",font=("Monospaced",20),
                                  fg="white",bg="blue")
        submit_button = Button(main_window2,text="Submit",command=self.sheet_condition,font=("Monospaced",14))

        #Place widget
        select_item_label.place(x=50,y=0)
        submit_button.place(x=120,y=120)
        main_window2.mainloop()

    def open_file_ok2s_and_cross_section(self):
        information = msgbox.showinfo(title="Information",message="Please open OK2S file")
        ok2s_excel_file = fd.askopenfilename()
        information = msgbox.showinfo(title="Information",message="Please open ANC file")
        anc_excel_file = fd.askopenfilename()
        self.sheet_condition(ok2s_excel_file,anc_excel_file)

    def sheet_condition(self, ok2s_excel_file, anc_excel_file):
        pass

    def check_revision(self):
        pass

    def cross_section(self):
        pass

    def solder_mask_coverage(self):
        pass

    def save_ok2s_workbook(self):
        pass

if __name__ == "__main__":
    window = AncWindow(None)
