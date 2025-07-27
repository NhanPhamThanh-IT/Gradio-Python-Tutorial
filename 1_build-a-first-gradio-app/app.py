"""
app.py

This is a simple Gradio app that adds two numbers together.
It takes two numeric inputs and returns their sum as output.
"""

import gradio as gr

# Function to add two numbers
def add_numbers(num1, num2):
    return num1 + num2

# Create a Gradio interface
interface = gr.Interface(
    fn=add_numbers,
    inputs=[
        gr.Number(label="Number 1"),
        gr.Number(label="Number 2")
    ],
    outputs=gr.Number(label="Sum")
)

if __name__ == "__main__":
    # Launch the Gradio app
    interface.launch()