def binary_search(sorted_list,value):
    '''
    if specified_key exists in sorted_list,return its sequence number
    if not, return None

    here we assume the list is sorted "from smallest to largest" before input
    '''
    low = 0
    high = len(sorted_list) - 1

    while low <= high:
        mid = (low + high) / 2 # as integar
        guess = sorted_list[mid]
        if guess == value:
            return mid
        elif value > guess:
            low = mid + 1
        elif value < guess:
            high = mid -1
    return None


list1 = [1,3,5,6,8,90,]
print binary_search(list1,6)
print binary_search(list1,10)
