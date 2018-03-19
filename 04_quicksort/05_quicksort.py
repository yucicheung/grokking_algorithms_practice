def quicksort(arr):
	if len(arr)<2:
		return arr
	else:
		pivot = arr[0]
		less = [i for i in arr[1:] if i <= pivot]
		greater = [i for i in arr[1:] if i > pivot]
		return quicksort(less)+[pivot]+quicksort(greater)


arrs = [[],[1],[1,3,3,3,2],[1,2,3,5],[4,5,67,1,23],[12,2]]
for arr in arrs:
	print 'array: {}'.format(arr),
	print 'quicksort: {}'.format(quicksort(arr))
