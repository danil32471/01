import time
print('DDos Prank')
time.sleep(2)
print('by Danil')
time.sleep(2)
print('введите скорость. 1 - 5')
a = int(input(''))
c = str(input('введите сайт '))
b = a * 1000
d = 0
if a == 1:
	for i in range(b):
		print('DDos ', c)
		time.sleep(0.1)
		d += 1
if a == 2:
	for i in range(b):
		print('DDos ', c)
		time.sleep(0.01)
		d += 1
if a == 3:
	for i in range(b):
		print('DDos ', c)
		time.sleep(0.001)
		d += 1
if a == 4:
	for i in range(b):
		print('DDos ', c)
		time.sleep(0.0001)
		d += 1
if a == 5:
	for i in range(b):
		print('DDos ', c)
		time.sleep(0.00001)
		d += 1
if d == b:
	print('сайт лёг спать')
