driving = input('請問你有開過車嗎？')
if driving != '有' and driving != '沒有':
	print('只能輸入 有/沒有')
	raise SystemExit

age = input('你的年齡是？')
age = int(age)
if driving == '有':
	if age >= 18:
		print('好的沒問題')
	else:
		print('咦 你怎麼會開過車？')
elif driving == '沒有':
	if age >= 18:
		print('可以考駕照囉！會開車很方便')
	else:
		print('再過', 18-age , '年就可以考駕照囉！')