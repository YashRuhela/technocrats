import os
import tkinter as tk
from tkinter import messagebox, Label, Radiobutton, IntVar, Button

# Function to handle button clicks
def button_click(file_name):
    quiz_window(file_name)

# Function to create a quiz window
def quiz_window(file_name):
    quiz_window = tk.Toplevel(root)
    quiz_window.title(f"Welcome to {file_name} Quiz")

    # Read the quiz file
    folder_path = "Python Quiz"  # Replace with your folder path
    file_path = os.path.join(folder_path, f"{file_name}.txt")
    
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    questions = []
    options = []
    answers = []
    
    # Parsing the file content
    current_question = ""
    current_options = []
    for line in lines:
        line = line.strip()
        if line.startswith("Question :- "):
            if current_question:
                questions.append(current_question)
                options.append(tuple(current_options))
            current_question = line[len("Question :- "):]
            current_options = []
        elif line.startswith("a) "):
            current_options.append(line[len("a) "):])
        elif line.startswith("correct option :- "):
            answers.append(line[-1])

    # Add the last question
    if current_question:
        questions.append(current_question)
        options.append(tuple(current_options))

    # Variables to store user's answers
    current_question_index = 0
    user_answers = [None] * len(questions)

    # Function to display the current question
    def show_question(question_num):
        nonlocal current_question_index
        current_question_index = question_num
        question_label.config(text=questions[question_num])
        for i in range(4):
            option_labels[i].config(text=options[question_num][i])
        if user_answers[question_num] is not None:
            answer_var.set(user_answers[question_num])
        else:
            answer_var.set(-1)

    # Function to handle "Next" button click
    def next_question():
        if current_question_index < len(questions) - 1:
            current_question_index += 1
            show_question(current_question_index)

    # Function to handle "Previous" button click
    def prev_question():
        if current_question_index > 0:
            current_question_index -= 1
            show_question(current_question_index)

    # Function to handle radio button selection
    def select_answer(value):
        user_answers[current_question_index] = value

    # Create widgets for the quiz window
    question_label = Label(quiz_window, text="", wraplength=400, justify="left")
    question_label.pack()

    answer_var = IntVar()
    answer_var.set(-1)

    option_labels = []
    for i in range(4):
        option_label = Radiobutton(quiz_window, text="", variable=answer_var, value=i, command=lambda i=i: select_answer(i))
        option_labels.append(option_label)
        option_label.pack()

    next_button = Button(quiz_window, text="Next", command=next_question)
    next_button.pack()

    prev_button = Button(quiz_window, text="Previous", command=prev_question)
    prev_button.pack()

    show_question(current_question_index)

# Function to list files in the folder and create buttons
def list_files():
    folder_path = "Python Quiz"  # Replace with your folder path
    files = os.listdir(folder_path)
    
    for file in files:
        if file.endswith(".txt"):
            # Remove the file extension and create a button for each file
            file_name = os.path.splitext(file)[0]
            button = tk.Button(root, text=file_name, command=lambda f=file_name: button_click(f))
            button.pack()

# Create the main application window
root = tk.Tk()
root.title("Python Quiz")

# Label at the top
label = tk.Label(root, text="Welcome to Python Quiz")
label.pack()

# List files in the folder and create buttons
list_files()

# Start the GUI event loop
root.mainloop()
