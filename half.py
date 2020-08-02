def subsetSum(array):
    if len(array)%2==0:
        i = 0
        sum_1 = 0
        while i < len(array)//2:
            sum_1 = sum_1 + array[i]
            i = i + 1
        j = len(array)-1
        sum_2 = 0
        while j >= len(array)//2:
            sum_2 = sum_2+array[j]
            j = j - 1
        k=2
        print(max(array))
        if sum_1==sum_2:
            return True
        else:
            return False
    else:
        return  False
print(subsetSum([1,2,3,4,5,6]))
