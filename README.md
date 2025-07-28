# <div align="center">🧩 Gradio Python Tutorial 🧩</div>

<div align="center">

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/) [![Gradio](https://img.shields.io/badge/Gradio-Latest-orange.svg)](https://gradio.app/) [![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE) [![GitHub](https://img.shields.io/badge/GitHub-Open%20Source-lightgrey.svg)](https://github.com/) [![Tutorial](https://img.shields.io/badge/Tutorial-8%20Examples-brightgreen.svg)](https://github.com/) [![Status](https://img.shields.io/badge/Status-Maintained-brightgreen.svg)](https://github.com/)

</div>

<div align="justify">

A comprehensive tutorial repository for building interactive machine learning interfaces using Gradio in Python. This project provides step-by-step examples from basic to advanced components, helping developers quickly prototype and deploy AI models with user-friendly UIs for testing and sharing.

## 📚 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Tutorial Examples](#tutorial-examples)
- [Features](#features)
- [Getting Started](#getting-started)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

Gradio is a Python library that makes it easy to create customizable web interfaces for machine learning models and data science workflows. This tutorial covers essential Gradio components and demonstrates how to build interactive applications for various use cases.

## 🔧 Prerequisites

- Python 3.7 or higher
- pip (Python package installer)
- Basic knowledge of Python programming

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/Gradio-Python-Tutorial.git
   cd Gradio-Python-Tutorial
   ```

2. **Install required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Tutorial Examples

### 1. Build Your First Gradio App
**Location:** `1_build-a-first-gradio-app/`

A simple introduction to Gradio that demonstrates basic number addition functionality.

**Features:**
- Basic Gradio interface setup
- Number input components
- Simple function integration

**Code Example:**
```python
import gradio as gr

def add_numbers(num1, num2):
    return num1 + num2

interface = gr.Interface(
    fn=add_numbers,
    inputs=[
        gr.Number(label="Number 1"),
        gr.Number(label="Number 2")
    ],
    outputs=gr.Number(label="Sum")
)
```

**Run the example:**
```bash
cd 1_build-a-first-gradio-app
python app.py
```

### 2. Text Box Component
**Location:** `2_how-to-create-a-text-box/`

Learn how to create and use text input components in Gradio applications.

**Features:**
- Text input and output handling
- String manipulation functions
- Real-time text processing

**Code Example:**
```python
def revert_text(text):
    return text[::-1]

interface = gr.Interface(
    fn=revert_text,
    inputs=gr.Textbox(label="Enter text to reverse"),
    outputs=gr.Textbox(label="Reversed text")
)
```

### 3. Slider Component
**Location:** `3_how-to-create-a-slider/`

Explore slider inputs for numerical value selection with range constraints.

**Features:**
- Range-based input selection
- Real-time value processing
- Mathematical operations

**Code Example:**
```python
def square(x):
    return x ** 2

interface = gr.Interface(
    fn=square,
    inputs=gr.Slider(minimum=0, maximum=100, label="Select a number"),
    outputs=gr.Textbox(label="Squared value")
)
```

### 4. Dropdown Component
**Location:** `4_how-to-create-a-dropdown/`

Create interactive dropdown menus for option selection in calculator applications.

**Features:**
- Multiple choice selection
- Conditional logic implementation
- Calculator functionality

**Code Example:**
```python
def calculate(number1, number2, operation):
    if operation == "Addition":
        return number1 + number2
    elif operation == "Subtraction":
        return number1 - number2
    # ... more operations

interface = gr.Interface(
    fn=calculate,
    inputs=[
        gr.Number(label="Number 1"),
        gr.Number(label="Number 2"),
        gr.Dropdown(choices=["Addition", "Subtraction", "Multiplication", "Division"])
    ],
    outputs=gr.Textbox(label="Result")
)
```

### 5. File Upload Component
**Location:** `5_file-upload-in-gradio/`

Handle file uploads and perform basic file analysis operations.

**Features:**
- File upload functionality
- File metadata extraction
- Basic file processing

**Code Example:**
```python
def analyze_file(file):
    if file is None:
        return "No file uploaded."
    return f"File Name: {file.name}"

interface = gr.Interface(
    fn=analyze_file,
    inputs=gr.File(label="Upload File"),
    outputs=gr.Textbox(label="Analysis Result")
)
```

### 6. Image Upload and Processing
**Location:** `6_upload-an-image-in-gradio/`

Work with image uploads and perform image processing operations like resizing.

**Features:**
- Image upload and display
- Image resizing functionality
- PIL integration
- Dynamic size adjustment

**Code Example:**
```python
def resize_image(image, width, height):
    if image is None:
        return None
    return image.resize((width, height))

interface = gr.Interface(
    fn=resize_image,
    inputs=[
        gr.Image(type="pil", label="Upload Image"),
        gr.Slider(minimum=50, maximum=1000, value=300, step=10, label="Width"),
        gr.Slider(minimum=50, maximum=1000, value=300, step=10, label="Height")
    ],
    outputs=gr.Image(type="pil", label="Resized Image")
)
```

### 7. Radio Button Component
**Location:** `7_how-to-create-a-radio-button/`

Create single-choice selection interfaces using radio buttons.

**Features:**
- Single choice selection
- Quiz-like functionality
- Conditional responses

**Code Example:**
```python
def check_answer(selected_language):
    correct_answer = "Python"
    if selected_language == correct_answer:
        return "Correct! Python is known for its simplicity and readability."
    else:
        return f"Incorrect. The correct answer is {correct_answer}."

interface = gr.Interface(
    fn=check_answer,
    inputs=gr.Radio(
        choices=["Python", "JavaScript", "Java"],
        label="Which programming language is known for its simplicity and readability?"
    ),
    outputs=gr.Textbox("Your result:")
)
```

### 8. Checkbox Group Component
**Location:** `8_how-to-create-a-checkbox-group/`

Implement multiple-choice selection using checkbox groups.

**Features:**
- Multiple choice selection
- List processing
- Dynamic response generation

**Code Example:**
```python
def favorite_colors(selected_colors):
    if not selected_colors:
        return "You didn't select any colors."
    return f"You selected: {', '.join(selected_colors)}"

interface = gr.Interface(
    fn=favorite_colors,
    inputs=gr.CheckboxGroup(
        choices=["Red", "Green", "Blue", "Yellow"],
        label="Select your favorite colors",
        type="value"
    ),
    outputs="text"
)
```

## ✨ Features

- **Progressive Learning:** Start with basic concepts and advance to complex components
- **Real-world Examples:** Each tutorial demonstrates practical use cases
- **Interactive Components:** Learn to use various Gradio input/output components
- **Code Documentation:** Well-commented code with clear explanations
- **Easy Setup:** Simple installation and execution process
- **Modular Structure:** Each example is self-contained and independent

## 🎓 Getting Started

1. **Choose a tutorial:** Start with the first example and progress through each one
2. **Run the code:** Execute `python app.py` in each tutorial directory
3. **Experiment:** Modify the code to understand how different components work
4. **Build your own:** Use the examples as templates for your own projects

## 📁 Project Structure

```
Gradio-Python-Tutorial/
├── 1_build-a-first-gradio-app/
│   └── app.py                 # Basic number addition app
├── 2_how-to-create-a-text-box/
│   └── app.py                 # Text reversal app
├── 3_how-to-create-a-slider/
│   └── app.py                 # Number squaring with slider
├── 4_how-to-create-a-dropdown/
│   └── app.py                 # Calculator with dropdown
├── 5_file-upload-in-gradio/
│   └── app.py                 # File upload and analysis
├── 6_upload-an-image-in-gradio/
│   └── app.py                 # Image upload and resizing
├── 7_how-to-create-a-radio-button/
│   └── app.py                 # Quiz with radio buttons
├── 8_how-to-create-a-checkbox-group/
│   └── app.py                 # Multiple choice with checkboxes
├── requirements.txt            # Python dependencies
├── README.md                  # This file
└── LICENSE                    # Project license
```

## 🛠️ Key Components Covered

### Input Components
- **Number:** For numerical inputs
- **Textbox:** For text input and output
- **Slider:** For range-based selection
- **Dropdown:** For single choice from options
- **File:** For file uploads
- **Image:** For image uploads and processing
- **Radio:** For single choice selection
- **CheckboxGroup:** For multiple choice selection

### Output Components
- **Textbox:** For text output
- **Number:** For numerical output
- **Image:** For image display
- **Text:** For simple text responses

## 🚀 Advanced Usage

After completing the tutorials, you can:

1. **Combine Components:** Mix different input/output components in a single app
2. **Add Custom Logic:** Implement your own functions and algorithms
3. **Style Your Apps:** Customize the appearance using Gradio's theming options
4. **Deploy Models:** Use Gradio to deploy machine learning models
5. **Create Dashboards:** Build interactive dashboards for data visualization

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch:** `git checkout -b feature/amazing-feature`
3. **Commit your changes:** `git commit -m 'Add amazing feature'`
4. **Push to the branch:** `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Contribution Guidelines
- Add clear documentation for new examples
- Include comments in code for better understanding
- Test your examples before submitting
- Follow the existing code style and structure

## 📖 Additional Resources

- [Gradio Official Documentation](https://gradio.app/docs/)
- [Gradio GitHub Repository](https://github.com/gradio-app/gradio)
- [Gradio Examples Gallery](https://gradio.app/gallery)
- [Gradio Community](https://discord.gg/feTf9x3ZSB)

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- The Gradio team for creating such an amazing library
- The open-source community for continuous support and contributions
- All contributors who help improve this tutorial

</div>

---

<div align="center">

*This tutorial is designed to help you master Gradio and build amazing interactive applications. Start with the basics and work your way up to creating sophisticated machine learning interfaces.*

**Happy Coding! 🎉**

</div>
