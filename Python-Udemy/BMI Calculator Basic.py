height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

#Write your code below this line 👇
BMI = float(weight) / (float(height) * float(height))
print(int(BMI))
#Formula: BMI= weight/(height**2)
#type of weight and height: string -> float
