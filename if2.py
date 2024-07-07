# else if 另外如果
age = input('Please enter your age : ')
age = int(age)
if age < 13 :
	print('elementry school')
elif age > 13 and age < 18 :
	print('junior and senior high scool')
elif age > 18 and age < 22 :
	print('university')
else :
	print('social elite')