import tkinter as tk
import numpy as np

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.configure(bg="black")

        self.expression = ""
        self.result_var = tk.StringVar(value="0")

        self.create_display()
        self.create_buttons()

    def create_display(self):
        tk.Label(
            self.root, textvariable=self.result_var, 
            font=("Arial", 30), bg="black", fg="white", 
            anchor="e", padx=10
        ).grid(row=0, column=0, columnspan=4, sticky="nsew")

    def create_buttons(self):
        buttons = [
            ("AC", "light gray"), ("±", "light gray"), 
            ("%", "light gray"), ("÷", "orange"),
            ("7", "gray"), ("8", "gray"), ("9", "gray"), ("x", "orange"),
            ("4", "gray"), ("5", "gray"), ("6", "gray"), ("-", "orange"),
            ("1", "gray"), ("2", "gray"), ("3", "gray"), ("+", "orange"),
            ("0", "gray", 2), (".", "gray"), ("=", "orange")
        ]

        row, col = 1, 0
        for btn in buttons:
            text, color = btn[0], btn[1]
            colspan = btn[2] if len(btn) > 2 else 1

            tk.Button(
                self.root, text=text, bg=color, fg="black" if color != "orange" else "white",
                font=("Arial", 18), width=3, height=1, relief="flat",
                command=lambda t=text: self.on_button_click(t)
            ).grid(row=row, column=col, columnspan=colspan, sticky="nsew")

            col += colspan
            if col > 3:
                col, row = 0, row + 1

        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, button_text):
        if button_text == "AC":
            self.expression = ""
            self.result_var.set("0")
        elif button_text == "±":
            self.expression = f"-{self.expression}" if not self.expression.startswith("-") else self.expression[1:]
            self.result_var.set(self.expression)
        elif button_text == "=":
            try:
                result = eval(self.expression.replace("x", "*").replace("÷", "/"))
                self.result_var.set(str(np.round(result, 4)))
                self.expression = str(result)
            except:
                self.result_var.set("Error")
                self.expression = ""
        else:
            if self.result_var.get() == "0" and button_text not in ["+", "-", "x", "÷", "%", "±"]:
                self.expression = button_text
            else:
                self.expression += button_text
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    Calculator(root)
    root.mainloop()
