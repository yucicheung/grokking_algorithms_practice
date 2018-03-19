def recursive_sum(arr):
	'''
	recursive way to calculate sum
	'''
	if arr==[]:
		return 0
	else:
		return arr.pop() + sum(arr)


def loop_sum(arr):
	'''
	loop way to calculate sum
	'''
	sum = 0
	for i in arr:
		sum+=i
	return sum


if __name__=='__main__':
	arrays = [[],[20],[1,2,4,5,6],]
	for arr in arrays:
		print 'array is {}:'.format(arr)
		print 'loop sum is {},'.format(loop_sum(arr)),
		print 'recursive sum is {}.'.format(recursive_sum(arr))
