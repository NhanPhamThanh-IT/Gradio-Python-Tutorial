"""
app.py

This script creates a simple Gradio application with a slider input that allows users to select a number. The selected number is then squared and displayed in a textbox.
The application uses the Gradio library to create the user interface.
"""

import gradio as gr

# Function to square the input value
def square(x):
    """Returns the square of the input value."""
    return x ** 2

# Create a Gradio interface with a slider input
interface = gr.Interface(
    fn=square,  # Function to call when the slider value changes
    inputs=gr.Slider(minimum=0, maximum=100, label="Select a number"),
    outputs=gr.Textbox(label="Squared value")
)

if __name__ == "__main__":
    # Launch the Gradio interface
    interface.launch()
