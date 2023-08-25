from tkinter import *

def classify_bmi(bmi):
    if bmi > 40:
        return "Obese Class 3"
    elif 35 < bmi <= 40:
        return "Obese Class 2"
    elif 30 < bmi <= 35:
        return "Obese Class"
    elif 25 < bmi <= 30:
        return "Overweight"
    elif 18.5 < bmi <= 25:
        return "Normal"
    elif 17 < bmi <= 18.5:
        return "Mild Thinness"
    elif 16 < bmi <= 17:
        return "Moderate Thinness"
    elif 0 < bmi <=16:
        return "Severe Thinness"
    else:
        return "Invalid"

def calculate_bmi():

    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get()) / 100
        if weight == 0:
            result_label.config(text="Weight can't be zero!")
            return
        bmi = round(weight / (height * height), 2)
        bmi_category = classify_bmi(bmi)
        result_label.config(text=f"Your BMI is {bmi}. \nYou are {bmi_category}.")
    except ValueError:
        result_label.config(text="Enter a valid number!")
    except ZeroDivisionError:
        result_label.config(text="Height can't be zero!")

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=250)
window.iconbitmap("C:/Users/okana/Masaüstü/icon.ico")

weight_label = Label(window, text="Enter Your Weight (kg)")
weight_label.pack(pady=10)

weight_entry = Entry(window, width=25)
weight_entry.pack()

height_label = Label(window, text="Enter Your Height (cm)")
height_label.pack(pady=10)

height_entry = Entry(window, width=25)
height_entry.pack()

calculate_button = Button(window, text="Calculate", command=calculate_bmi)
calculate_button.pack(pady=10)

result_label = Label(window, text="Click the button to calculate")
result_label.pack()

window.mainloop()