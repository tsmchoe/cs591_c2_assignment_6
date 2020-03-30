def Reverse_Pairs(arr):
    count = 0;
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i < j:
                if arr[i] > 2*arr[j]:
                    count += 1


    return count