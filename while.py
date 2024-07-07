# while loop 迴圈
x = 5 
while x < 10 :
	print('x < 10')
	print('I stuck in the loop!')
	x = x + 1
print('i escape the loop!')

# while True
while True :
    mode = input('Please enter the game mode : ')
    if mode == 'quit' : #離開 
	    print('Leaving the game')
	    break #跳出迴圈
    elif mode == 'Easy' : 
        print('Let us start the game! (Easy) ')
        break 
    elif mode == 'Difficult' : 
        print('Let us start the game! (Difficult)')
        break 
    else : 
        print('Choose Easy/Difficult/quit ONLY')
