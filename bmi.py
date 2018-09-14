height = input ("請輸入你的身高： ")
weight = input ("請輸入你的體重： ")
height = float(height)
weight = float(weight)
bmi = weight / ((height / 100) * (height / 100))
bmi = float(bmi)
if bmi < 18.5:
	print('你的體重過輕了哦！')
elif bmi >= 18.5 and bmi < 24:
	print('BMI非常標準哦！')
elif bmi >= 24 and bmi < 27:
	print('過重')
elif bmi >= 27 and bmi < 30:
	print('中度肥')
else:
	print('重度肥胖')
