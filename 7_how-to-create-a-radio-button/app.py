"""
app.py

This file contains a simple Gradio application that demonstrates how to create a radio button for user input.
"""

import gradio as gr

# This code creates a simple Gradio application with a radio button for selecting a programming language.
def check_answer(selected_language):
    correct_answer = "Python"
    if selected_language == correct_answer:
        return "Correct! Python is known for its simplicity and readability."
    else:
        return f"Incorrect. The correct answer is {correct_answer}."

# Create a Gradio interface for a radio button question
interface = gr.Interface(
    fn=check_answer,
    inputs=gr.Radio(
        choices=["Python", "JavaScript", "Java"],
        label="Which programming language is known for its simplicity and readability?"
    ),
    outputs=gr.Textbox("Your result:"),
)

if __name__ == "__main__":
    # Launch the Gradio interface
    interface.launch()