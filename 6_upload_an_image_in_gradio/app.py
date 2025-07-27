"""
app.py - A Gradio application to upload and resize an image.

This application allows users to upload an image and specify the desired width and height for resizing. The resized image is then displayed as output.
"""

import gradio as gr

# Function to resize an image
def resize_image(image, width, height):
    """
    Resize the uploaded image to the specified width and height.

    Args:
        image (PIL.Image): The uploaded image.
        width (int): The desired width of the resized image.
        height (int): The desired height of the resized image.

    Returns:
        PIL.Image: The resized image.
    """
    if image is None:
        return None
    return image.resize((width, height))

# Create a Gradio interface for resizing images
interface = gr.Interface(
    fn=resize_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Slider(minimum=50, maximum=1000, value=300, step=10, label="Width"),
        gr.Slider(minimum=50, maximum=1000, value=300, step=10, label="Height")
    ],
    outputs=gr.Image(type="pil", label="Resized Image")
)

if __name__ == "__main__":
    # Launch the Gradio interface
    interface.launch()