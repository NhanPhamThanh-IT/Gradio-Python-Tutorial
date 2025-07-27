"""
app.py

This is a simple Gradio app that reverses the input text.
It takes a text input and returns the reversed text as output.
"""

import gradio as gr

# Function to reverse text
def revert_text(text):
    """Reverses the input text."""
    return text[::-1]

# Create a Gradio interface
interface = gr.Interface(
    fn=revert_text,
    inputs=gr.Textbox(label="Enter text to reverse"),
    outputs=gr.Textbox(label="Reversed text")
)

if __name__ == "__main__":
    # Launch the Gradio app
    interface.launch()