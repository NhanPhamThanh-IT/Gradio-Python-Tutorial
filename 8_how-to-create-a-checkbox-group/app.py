"""
app.py

This file contains a simple Gradio application that demonstrates how to create a checkbox group for user input.
"""

import gradio as gr

# This function processes the selected colors from the checkbox group.
# It returns a message indicating which colors were selected.
def favorite_colors(selected_colors):
    """
    This function takes a list of selected colors and returns a message.
    If no colors are selected, it returns a different message.

    Args:
        selected_colors (list): A list of colors selected by the user.
    
    Returns:
        str: A message indicating the selected colors or that no colors were selected.
    """
    if not selected_colors:
        return "You didn't select any colors."
    return f"You selected: {', '.join(selected_colors)}"

# Create a Gradio interface for a checkbox group question
iface = gr.Interface(
    fn=favorite_colors,
    inputs=gr.CheckboxGroup(
        choices=["Red", "Green", "Blue", "Yellow"],
        label="Select your favorite colors",
        type="value"
    ),
    outputs="text"
)

if __name__ == "__main__":
    # Launch the Gradio interface
    iface.launch()