# password-retry 密碼重試程式
correct_password = 'a19990820'
attempts = 0
max_attempt = 3
while attempts < 3 :
	password = input('Please enter the password: ')
	if password == correct_password :
		print('Password is correct! You can log in.')
		break
	else :
		attempts += 1
		print('Wrong! Please enter the password again, you have', max_attempt - attempts , 'chance(s). ')
		if attempts == max_attempt :
			print('Sorry! you try too many times wrong! Try again later!')
			