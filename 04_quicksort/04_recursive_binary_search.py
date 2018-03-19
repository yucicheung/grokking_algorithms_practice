def binary_search(target, low, high, arr):
	if arr == []:
		return None
	elif low > high:
		return None
	else:
		mid = (low+high)/2
		mid_v = arr[mid]
		if target == mid_v:
			return mid
		elif target > mid_v:
			low = mid + 1
		else:
			high = mid - 1
		return binary_search(target,low,high,arr)


arrs = [[],[1],[1,3,4,5]]
target = 5
for arr in arrs:
	print 'arr is {},target {} is at {}.'.format(arr,target,binary_search(target,0,len(arr)-1,arr))
