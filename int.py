# int應用-型別轉換
# if age >= 18: 會失敗, 因為此18被視為整數, 所以要先用int轉換為整數
# 或是直接把'18'加上''讓它成字串,也可以進行比較
age = input('請輸入你的年齡 : ')
age = int(age)
if age >= 18:
    print('You can vote!')
else:
    print('Sorry! You cannot vote now')