def fact(i):
	if i==1 :
		return 1
	else:
		return i * fact(i-1)


if __name__ == '__main__':
	print fact(5)
