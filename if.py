# If 練習
# 收穫1: 可以應用針對不同答案的回覆(ex.心理測驗的分數與對應性格或生日星座指南)
# 收穫2: if fortune_teller = '0820': 後面一定要記得放: 可以想像成清單的開頭
# 收穫3: if 的裡面會有區塊, if下3行有空格是if內的block
# 收穫4: print('Wish you a good day') 不在if裡, 所以不管回答什麼都會印
# 收穫5: 可以再創建更深層的資料夾
# 收穫6: 雖然print('great! your mbti must be I type')在深沉資料夾,但即便回覆是16,仍會反映
# 收穫7: 按4下space鍵盤空格最標準, tab鍵也可以,但space是公定的, ctrl a時一目了然
fortune_teller = input('When is your birthday date?(only type date 1-31) : ')
if fortune_teller == '20':
    print('You sure are the netflix person who is addicted to the movie')
    print('Yellow would be your lucky color in 2024')
    print('This year is a lucky year for you, buy the lottery and you will be the big prize winner!')
    if fortune_teller > '15':
        print('Great! your mbti is I type')
    else : 
    	print('Your mbti is E type')
print('Wish you a good day')