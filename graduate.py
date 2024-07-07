# graduate - graduate qualification 
credit_points = input('How many credit points you have? (caculate to this semester) : ')
toeic = input('Do you score over 750 in Toeic test? (yes/no): ')
if toeic != 'yes' and toeic != 'no' :
	print('please reply in yes/no')
	raise SystemExit
credit_points = int(credit_points)
if credit_points >= 120 and toeic == 'yes' :
	print('Congratulation! You are qualify to graduate! ')
elif credit_points >= 120 and toeic == 'no' :
	print('Ooops, you still need to pass Toeic test with over 750 score to get the graduate certification.')
elif credit_points < 120 and toeic == 'yes' :
	print('Ooops, you still need to get more credit points to reach 120 for graduate certification.')
elif credit_points < 120 and toeic == 'no' :
	print('Ooops, you still need to get total 120 credits and Toeic test over 750 to get the graduate certification. ')