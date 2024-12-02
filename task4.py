import tkinter as tk
from tkinter import messagebox

# Function to calculate BMI
def calculate_bmi():
    try:
        weight = float(entry_weight.get())  # Get weight from the input field
        height = float(entry_height.get())  # Get height from the input field

        # Calculate BMI
        bmi = weight / (height ** 2)
        result_label.config(text=f"Your BMI is: {bmi:.2f}")

        # Determine the classification
        if bmi < 18.5:
            classification = "Underweight"
        elif 18.5 <= bmi < 24.9:
            classification = "Normal weight"
        elif 25 <= bmi < 29.9:
            classification = "Overweight"
        else:
            classification = "Obesity"

        classification_label.config(text=f"Classification: {classification}")

    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numeric values.")

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

# Set the window size
root.geometry("400x300")

# Weight label and input field
weight_label = tk.Label(root, text="Enter weight (kg):")
weight_label.pack(pady=10)

entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

# Height label and input field
height_label = tk.Label(root, text="Enter height (m):")
height_label.pack(pady=10)

entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Button to calculate BMI
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
calculate_button.pack(pady=20)

# Label to display the BMI result
result_label = tk.Label(root, text="Your BMI is: ")
result_label.pack(pady=5)

# Label to display the classification
classification_label = tk.Label(root, text="Classification: ")
classification_label.pack(pady=5)

# Start the GUI loop
root.mainloop()
