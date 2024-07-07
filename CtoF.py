# 攝氏溫度轉換成華氏溫度
custom_c = input('請輸入攝氏溫度')
custom_c = float(custom_c)
transit_f = custom_c * 9 / 5 + 32
print('華氏溫度為 : ' , transit_f)
custom_f = input('請輸入華氏溫度')
custom_f = float(custom_f)
transit_c = (custom_f - 32 ) *5 / 9
print('攝氏溫度為 : ' , transit_c)