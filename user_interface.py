import tkinter

class UI:

    def __init__(self):
        self.window = tkinter.Tk()
        self.window.title("Pixela")
        self.window.geometry("1100x800")

    def exit_window(self):
        self.window.mainloop()


ui = UI()
ui.exit_window()