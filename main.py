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
            BMI_label.config(text="Weight can't be zero!")
            return
        bmi = round(weight / (height * height), 2)
        bmi_category = classify_bmi(bmi)
        normal_weight = round(22 * (height*height), 2)
        lose_weight = abs(round(normal_weight-weight,2))

        if normal_weight > weight:
            message = "You need to gain"
        else:
            message = "You have to lose"

        BMI_label.config(text=f"Your BMI is {bmi}.")
        Class_label.config(text=f"You are {bmi_category}.")
        normal_label.config(text=f"Your normal weight : {normal_weight}.", fg="green")
        lose_label.config(text=f"{message} {lose_weight} kilos!", fg="red")
    except ValueError:
        BMI_label.config(text="Enter a valid number!")
    except ZeroDivisionError:
        BMI_label.config(text="Height can't be zero!")

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250, height=270)
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

BMI_label = Label(window, text="Click the button to calculate!")
BMI_label.pack()

Class_label = Label(window, text="")
Class_label.pack()

normal_label = Label(window, text="", fg="green")
normal_label.pack()

lose_label = Label(window, text="", fg="red")
lose_label.pack()


window.mainloop()