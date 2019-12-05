# linear search
# brute force search, list does not have to be sorted

def linear_search(l,e):
    found  = False
    for i in range(len(l)):
        if e== l[i]:
            return True
    return found


#in a sorted list, from smallest to biggest
# increasing order
def search(l,e):
    for i in range(len(l)):
        if l[i] == e:
            return True
        if l[i] > e:
            return False
    return False

#  bisection search 

def bisect_search(L, e):
    def bisearch_helper(L, e, low, high):
        if low == high:
            return L[low] == e
        mid = (high + low) // 2
        if L[mid] == e:
            return True
        elif L[mid] > e:
            if low == mid: # nothing left to search, but seems unnecessary
                return False
            else:
                return bisearch_helper(L,e, low, mid-1)
        else:
            return bisearch_helper(L, e, mid+1, high)

    if len(L)==0:
        return False
    else:
        return bisearch_helper(L, e, 0, len(L)-1)

# when is it reasonable to sort a list before searching for elements?
# when we need to do multiple searches
def bubble_sort(L, e):  # complexity n squared 
    swap = False
    while not swap:
        swap = True
        for j in range(1, len(L)):
            if L[j-1] > L[j]:
                swap = False
                L[j], L[j-1] = L[j-1], L[j]

def selection_sort(L: list, e:int): # n squared 
    suffixSt = 0
    while suffixSt != len(L):
        for i in range (suffixSt, len(L)):
            if L[i] < L[suffixSt]:
                L[suffixSt], L[i] =  L[i], L[suffixSt]
        suffixSt += 1

def merge_sort(L): # complexity nlogn 
    # divide and conquer
    def merge(left, right):
        result = []
        i, j = 0, 0
        while (i < len(left)) and (j < len(right)):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j < len(right):
            result.append(right[j])
            j += 1
        print('merge: ' + str(left) + '&' + str(right) + 'to' + str(result))
        return result
    print('merge sort: ' + str(L))
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L)//2
        left = merge_sort(L[:middle]) 
        right = merge_sort(L[middle:]) 
        return merge(left,right)
    

merge_sort([1,2,3,5,6,7,13,18,25])
            

    
