driving = input('請問你有沒有開過車：')
if driving != '有' and driving != '沒有':
	print('不要來亂')
	raise SystemExit
	
age = input('請問你的年齡？')
if driving == '有':
	if int(age) >= 18:
		print('你的年齡：', age, '可以開車囉')
	else:
		print('你的年齡：', age, '還不可以開車喔')
elif driving == '沒有':
	if int(age) >= 18:
		print('還不去考駕照？')
	else:
		print('以後就可以考了')
	
	