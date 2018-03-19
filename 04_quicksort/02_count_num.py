def count_num(arr):
	'''
	recursive way to count the number of elements in a list.
	'''
	if arr==[]:
		return 0
	else:
		arr.pop()
		return 1 + count_num(arr)


if __name__=='__main__':
	arrs = [[],[1],[1,2,3,4,5,]]
	for arr in arrs:
		print 'array:{}'.format(arr)
		print 'number of elements is {}'.format(count_num(arr))

