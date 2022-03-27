import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.configure(background="white")
        self.master.title("Simple Calculator")
        self.master.geometry("270x150")

        self.result = tk.StringVar()
        self.input_text = ''
    
        self.expression_field = tk.Entry(self.master, textvariable=self.result, bg='white')
        self.expression_field.grid(columnspan=4, ipadx=70)

        self.create_widgets()

    def clear(self):
        self.input_text = ""
        self.result.set("")

    def create_widgets(self):
        button1 = tk.Button(self.master, text=' 1 ', fg='black', bg='lightgray',
                        command=lambda: self.press(1), height=1, width=7)
        button1.grid(row=2, column=0)
    
        button2 = tk.Button(self.master, text=' 2 ', fg='black', bg='lightgray',
                        command=lambda: self.press(2), height=1, width=7)
        button2.grid(row=2, column=1)
    
        button3 = tk.Button(self.master, text=' 3 ', fg='black', bg='lightgray',
                        command=lambda: self.press(3), height=1, width=7)
        button3.grid(row=2, column=2)
    
        button4 = tk.Button(self.master, text=' 4 ', fg='black', bg='lightgray',
                        command=lambda: self.press(4), height=1, width=7)
        button4.grid(row=3, column=0)
    
        button5 = tk.Button(self.master, text=' 5 ', fg='black', bg='lightgray',
                        command=lambda: self.press(5), height=1, width=7)
        button5.grid(row=3, column=1)
    
        button6 = tk.Button(self.master, text=' 6 ', fg='black', bg='lightgray',
                        command=lambda: self.press(6), height=1, width=7)
        button6.grid(row=3, column=2)
    
        button7 = tk.Button(self.master, text=' 7 ', fg='black', bg='lightgray',
                        command=lambda: self.press(7), height=1, width=7)
        button7.grid(row=4, column=0)
    
        button8 = tk.Button(self.master, text=' 8 ', fg='black', bg='lightgray',
                        command=lambda: self.press(8), height=1, width=7)
        button8.grid(row=4, column=1)
    
        button9 = tk.Button(self.master, text=' 9 ', fg='black', bg='lightgray',
                        command=lambda: self.press(9), height=1, width=7)
        button9.grid(row=4, column=2)
    
        button0 = tk.Button(self.master, text=' 0 ', fg='black', bg='lightgray',
                        command=lambda: self.press(0), height=1, width=7)
        button0.grid(row=5, column=0)
    
        plus = tk.Button(self.master, text=' + ', fg='black', bg='lightgray',
                    command=lambda: self.press("+"), height=1, width=7)
        plus.grid(row=2, column=3)
    
        minus = tk.Button(self.master, text=' - ', fg='black', bg='lightgray',
                    command=lambda: self.press("-"), height=1, width=7)
        minus.grid(row=3, column=3)
    
        multiply = tk.Button(self.master, text=' * ', fg='black', bg='lightgray',
                        command=lambda: self.press("*"), height=1, width=7)
        multiply.grid(row=4, column=3)
    
        divide = tk.Button(self.master, text=' / ', fg='black', bg='lightgray',
                        command=lambda: self.press("/"), height=1, width=7)
        divide.grid(row=5, column=3)
    
        equal = tk.Button(self.master, text=' = ', fg='black', bg='lightgray',
                    command=self.equalpress, height=1, width=7)
        equal.grid(row=5, column=2)
    
        clear = tk.Button(self.master, text='Clear', fg='black', bg='lightgray',
                    command=self.clear, height=1, width=7)
        clear.grid(row=5, column='1')
    
        Decimal= tk.Button(self.master, text='.', fg='black', bg='lightgray',
                        command=lambda: self.press('.'), height=1, width=7)
        Decimal.grid(row=6, column=0)


    def press(self, num):
        self.input_text = "".join([self.input_text, str(num)])
        self.result.set(self.input_text)
 

    def equalpress(self):
        try:
            total = eval(self.input_text)
            total = str(total)
            self.result.set(total)
            self.input_text = ""
        except:
    
            self.result.set(" error ")
            self.input_text = ""

    # def get_command(self, task):
    #     if task == 'add':
    #         return self.__add_num
    #     elif task == 'sub':
    #         return self.__sub_num
    #     elif task == 'mult':
    #         return self.__mult_num
    #     elif task == 'div':
    #         return self.__div_num
    #     elif task == 'pow':
    #         return self.__pow_num
    #     elif task == 'remain':
    #         return self.__remain_num
    #     return

    # def __add_num(self, a, b):
    #     return a + b if a and b else 0
    # def __sub_num(self, a, b):
    #     return a - b if a and b else 0
    # def __mult_num(self, a, b):
    #     return a * b if a and b else 0
    # def __div_num(self, a, b):
    #     return a / b if a and b else 0
    # def __pow_num(self, a, b):
    #     return a ** b if a and b else 0
    # def __remain_num(self, a, b):
    #     return a % b if a and b else 0

if __name__ == '__main__':
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()