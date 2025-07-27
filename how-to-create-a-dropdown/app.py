"""
app.py

This script creates a simple calculator application using Gradio. It allows users to perform basic arithmetic operations (addition, subtraction, multiplication, and division) by selecting an operation from a dropdown menu.
It includes input fields for two numbers and a dropdown for selecting the operation. The result is displayed in a textbox.
"""

import gradio as gr

# Function to perform basic arithmetic operations
def calculate(number1, number2, operation):
    if operation == "Addition":
        return number1 + number2
    elif operation == "Subtraction":
        return number1 - number2
    elif operation == "Multiplication":
        return number1 * number2
    elif operation == "Division":
        return number1 / number2 if number2 != 0 else "Cannot divide by zero"

# Create a Gradio interface for a simple calculator with a dropdown for operations
interface = gr.Interface(
    fn=calculate,
    inputs=[
        gr.Number(label="Number 1"),
        gr.Number(label="Number 2"),
        gr.Dropdown(
            choices=["Addition", "Subtraction", "Multiplication", "Division"],
            label="Operation"
        )
    ],
    outputs=gr.Textbox(label="Result")
)

if __name__ == "__main__":
    # Launch the Gradio interface
    interface.launch()