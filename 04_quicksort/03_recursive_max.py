def find_max(arr):
	'''
	Use recursion to find the max.
	'''
	if arr==[]:
		return None
	elif len(arr)==1:
		return arr[0]
	else:
		max_ = arr[0]
		sub_max = find_max(arr[1:])
		if max_ < sub_max:
			max_ = sub_max
		return max_

if __name__=='__main__':
	arrs = [[1],[2,3,4,59,17],[]]
	for arr in arrs:
		print 'max of {}'.format(arr)
		print find_max(arr)
