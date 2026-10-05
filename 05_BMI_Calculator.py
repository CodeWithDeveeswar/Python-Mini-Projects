# BMI Calculator
# Calculate BMI using weight and height, then classify the BMI category.
# Concepts: INPUT • ARITHMETIC • CONDITIONALS • F-STRINGS

# 1. Inputs
weight = float(input("Weight (kg): "))
height = float(input("Height (m): "))

# 2. Calculation 
bmi = weight / (height ** 2)

# 3. Status Check
if bmi < 18.5:
    category = "Underweight"
elif bmi < 25:
    category = "Normal"
elif bmi < 30:
    category = "Overweight"
else:
    category = "Obese"   

# 4. Output 
print(f"{bmi:.1f} - {category}")