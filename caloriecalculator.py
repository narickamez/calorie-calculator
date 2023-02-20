import math


def calculate_calories():
  # Ask the user for their age
  age = int(input("Enter your age: "))

  # Ask the user for their sex
  sex = input("Enter your sex (male or female): ")

  # Ask the user for their height in inches
  height = int(input("Enter your height in inches: "))

  # Ask the user for their weight in pounds
  weight = int(input("Enter your weight in pounds: "))

  # Ask the user for their activity level
  activity_level = input("Enter your activity level (sedentary, lightly active, moderately active, very active, or extra active): ")

  # Convert height from inches to centimeters
  height_cm = height * 2.54

  # Calculate basal metabolic rate (BMR)
  if sex == "male":
    BMR = 66 + (6.23 * weight) + (12.7 * height_cm) - (6.8 * age)
  elif sex == "female":
    BMR = 655 + (4.35 * weight) + (4.7 * height_cm) - (4.7 * age)
  else:
    raise ValueError("Invalid sex")

  # Calculate daily calorie needs based on activity level
  if activity_level == "sedentary":
    calories = BMR * 1.2
  elif activity_level == "lightly active":
    calories = BMR * 1.375
  elif activity_level == "moderately active":
    calories = BMR * 1.55
  elif activity_level == "very active":
    calories = BMR * 1.725
  elif activity_level == "extra active":
    calories = BMR * 1.9
  else:
    raise ValueError("Invalid activity level")

  return calories

# Calculate and print the estimated daily calorie needs
calories = calculate_calories()
print(f"Your estimated daily calorie needs are {calories:.2f}.")

