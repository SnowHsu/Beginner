# import random
# 使用情境: 可以用在驗證碼產生和核對 
import random
r = random.randint(1,15)
count = 0
while True :
	count += 1    # count = count + 1
	number = input('Please guess a number : ')
	number = int(number)
	if number == r :
		print('Congrats! the number is ', r ,'that is correct!')
		break
	elif number > r :
		print('Wrong! hint: shouold be smaller.')
	else :
		print('Wrong! hint: shouold be bigger.')
	print('This is the' , count , 'time(s) you guess')

start = input('Please enter the start number : ')
end = input('Please enter the end number : ')
start = int(start)
end = int(end)
r1 = random.randint(start,end)
count1 = 0
while True :
	count1 += 1  
	number1 = input('Please guess a number : ')
	number1 = int(number1)
	if number1 == r1 :
		print('Congrats! the number is ', r1 ,'that is correct!')
		break
	elif number1 > r1 :
		print('Wrong! hint: shouold be smaller.')
	else :
		print('Wrong! hint: shouold be bigger.')
	print('This is the' , count1 , 'time(s) you guess')