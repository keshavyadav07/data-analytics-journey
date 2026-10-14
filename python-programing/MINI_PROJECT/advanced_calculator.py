
import tkinter as tk
import math
import ast
import operator


# ==========================================
# ADVANCED PYTHON GUI CALCULATOR
# Built with Tkinter
# ==========================================

class AdvancedCalculator:

    def __init__(self, root):
        self.root = root
        self.root.title("Advanced Calculator")
        self.root.geometry("380x570")
        self.root.resizable(False, False)
        self.root.configure(bg="#171717")

        self.expression = ""

        # Display
        self.display = tk.Entry(
            root,
            font=("Arial", 25),
            bg="#252525",
            fg="white",
            insertbackground="white",
            justify="right",
            relief="flat",
            bd=10
        )

        self.display.pack(
            fill="x",
            padx=15,
            pady=(20, 15),
            ipady=15
        )

        # Button container
        button_frame = tk.Frame(
            root,
            bg="#171717"
        )

        button_frame.pack(
            expand=True,
            fill="both",
            padx=10,
            pady=5
        )

        # Button layout
        buttons = [
            ["C", "⌫", "(", ")"],
            ["√", "x²", "1/x", "÷"],
            ["7", "8", "9", "×"],
            ["4", "5", "6", "−"],
            ["1", "2", "3", "+"],
            ["+/-", "0", ".", "="],
            ["%"]
        ]

        for row_index, row in enumerate(buttons):

            for col_index, text in enumerate(row):

                if text == "%":
                    column = 0
                    columnspan = 4
                else:
                    column = col_index
                    columnspan = 1

                button = tk.Button(
                    button_frame,
                    text=text,
                    font=("Arial", 15, "bold"),
                    bg=self.get_button_color(text),
                    fg="white",
                    activebackground="#555555",
                    activeforeground="white",
                    relief="flat",
                    cursor="hand2",
                    command=lambda value=text: self.on_button_click(value)
                )

                button.grid(
                    row=row_index,
                    column=column,
                    columnspan=columnspan,
                    sticky="nsew",
                    padx=4,
                    pady=4,
                    ipady=8
                )

        # Equal-sized buttons
        for col in range(4):
            button_frame.columnconfigure(
                col,
                weight=1,
                uniform="buttons"
            )

        for row in range(len(buttons)):
            button_frame.rowconfigure(
                row,
                weight=1,
                uniform="buttons"
            )

        # Keyboard support
        self.root.bind("<Key>", self.on_key_press)

        # Set initial focus
        self.display.focus_set()

    # ------------------------------------------
    # Button colors
    # ------------------------------------------

    def get_button_color(self, text):

        if text == "=":
            return "#00A878"

        elif text in ["+", "−", "×", "÷"]:
            return "#FF9500"

        elif text in ["C", "⌫"]:
            return "#B33939"

        elif text in ["√", "x²", "1/x", "%", "+/-", "(", ")"]:
            return "#444444"

        else:
            return "#303030"

    # ------------------------------------------
    # Handle button clicks
    # ------------------------------------------

    def on_button_click(self, value):

        current = self.display.get()

        try:

            if value == "C":
                self.display.delete(0, tk.END)
                self.expression = ""

            elif value == "⌫":
                self.display.delete(0, tk.END)
                self.display.insert(0, current[:-1])

            elif value == "=":
                self.calculate()

            elif value == "√":
                self.apply_function("sqrt")

            elif value == "x²":
                self.apply_function("square")

            elif value == "1/x":
                self.apply_function("reciprocal")

            elif value == "+/-":
                self.toggle_sign()

            elif value == "%":
                self.apply_function("percent")

            else:
                symbols = {
                    "×": "*",
                    "÷": "/",
                    "−": "-"
                }

                self.display.insert(
                    tk.END,
                    symbols.get(value, value)
                )

        except Exception:
            self.show_error()

    # ------------------------------------------
    # Safely evaluate mathematical expressions
    # ------------------------------------------

    def safe_calculate(self, expression):

        # Only allow mathematical operations.
        allowed_operators = {
            ast.Add: operator.add,
            ast.Sub: operator.sub,
            ast.Mult: operator.mul,
            ast.Div: operator.truediv,
            ast.Pow: operator.pow,
            ast.Mod: operator.mod,
            ast.UAdd: operator.pos,
            ast.USub: operator.neg
        }

        def evaluate(node):

            if isinstance(node, ast.Expression):
                return evaluate(node.body)

            elif isinstance(node, ast.Constant):
                if type(node.value) in (int, float):
                    return node.value

                raise ValueError("Invalid number")

            elif isinstance(node, ast.BinOp):
                operation = type(node.op)

                if operation not in allowed_operators:
                    raise ValueError("Invalid operation")

                left = evaluate(node.left)
                right = evaluate(node.right)

                if operation in (ast.Div, ast.Mod) and right == 0:
                    raise ZeroDivisionError

                # Avoid excessively large exponent calculations.
                if operation == ast.Pow:
                    if abs(right) > 1000:
                        raise ValueError("Exponent too large")

                result = allowed_operators[operation](
                    left,
                    right
                )

                if isinstance(result, complex):
                    raise ValueError("Complex numbers not supported")

                if isinstance(result, float) and not math.isfinite(result):
                    raise ValueError("Result out of range")

                return result

            elif isinstance(node, ast.UnaryOp):
                operation = type(node.op)

                if operation not in allowed_operators:
                    raise ValueError("Invalid operation")

                return allowed_operators[operation](
                    evaluate(node.operand)
                )

            else:
                raise ValueError("Invalid expression")

        tree = ast.parse(expression, mode="eval")
        result = evaluate(tree)

        if isinstance(result, (int, float)):
            if not math.isfinite(result):
                raise ValueError("Result out of range")

        return result

    # ------------------------------------------
    # Calculate expression
    # ------------------------------------------

    def calculate(self):

        expression = self.display.get().strip()

        if not expression:
            return

        try:

            result = self.safe_calculate(expression)

            # Remove unnecessary decimal zeros.
            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

        except Exception:
            self.show_error()

    # ------------------------------------------
    # Square root, square, reciprocal, percentage
    # ------------------------------------------

    def apply_function(self, function_name):

        try:

            expression = self.display.get().strip()

            if not expression:
                return

            number = self.safe_calculate(expression)

            if function_name == "sqrt":
                if number < 0:
                    raise ValueError("Negative square root")

                result = math.sqrt(number)

            elif function_name == "square":
                result = number ** 2

            elif function_name == "reciprocal":
                if number == 0:
                    raise ZeroDivisionError

                result = 1 / number

            elif function_name == "percent":
                result = number / 100

            else:
                return

            if isinstance(result, float) and not math.isfinite(result):
                raise ValueError("Result out of range")

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

        except Exception:
            self.show_error()

    # ------------------------------------------
    # Positive / Negative toggle
    # ------------------------------------------

    def toggle_sign(self):

        try:

            expression = self.display.get().strip()

            if not expression:
                return

            number = self.safe_calculate(expression)
            result = -number

            if isinstance(result, float) and result.is_integer():
                result = int(result)

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

        except Exception:
            self.show_error()

    # ------------------------------------------
    # Keyboard support
    # ------------------------------------------

    def on_key_press(self, event):

        key = event.char

        if key in "0123456789.+-*/()%":
            self.display.insert(tk.END, key)

        elif event.keysym in ("Return", "KP_Enter"):
            self.calculate()

        elif event.keysym == "BackSpace":
            current = self.display.get()

            self.display.delete(0, tk.END)
            self.display.insert(0, current[:-1])

        elif event.keysym == "Escape":
            self.display.delete(0, tk.END)

    # ------------------------------------------
    # Error handling
    # ------------------------------------------

    def show_error(self):

        self.display.delete(0, tk.END)
        self.display.insert(0, "Error")


# ==========================================
# Run the application
# ==========================================

if __name__ == "__main__":

    root = tk.Tk()

    calculator = AdvancedCalculator(root)

    root.mainloop()

