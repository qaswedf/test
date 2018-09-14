password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	enter_password = input('請輸入密碼： ')
	if password != enter_password:
		print('您所輸入的密碼錯誤')
		print('你還有', i,'次機會')
	else:
		print('你猜對密碼了！')
		break

