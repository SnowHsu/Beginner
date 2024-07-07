# BMI  BMI = 體重(公斤) / 身高2(公尺2)
weight = input('Please enter your weight (KG): ')
weight = float(weight)
height = input('Please enter your height (M): ')
height = float(height)
bmi = weight // height ** 2
print('Your BMI is' , bmi)
if bmi < 18.5 :
	print('Result : Underweight')
elif bmi >= 18.5 and bmi < 24 :
	print('Result : Normal')
elif bmi >=24 and bmi < 27 :
	print('Result : Overweight')
elif bmi >=27 and bmi < 30 :
	print('Result : Mild Obese')
elif bmi >= 30 and bmi < 35 :
	print('Result : Medium Obese')
else :
	print('Result : Extreme Obese')