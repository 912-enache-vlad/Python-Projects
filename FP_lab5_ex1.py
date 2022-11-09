import sys
#Solution with dinamic programming - Enache Vlad
def maximum_subarray(arr:list):
    maxSum = arr[0]
    for i in range(1, len(arr)):
        if arr[i] + maxSum < arr[i]: # the case when we start the sum again
            maxSum = arr[i]
        else:
            maxSum += arr[i]

    return maxSum

print(maximum_subarray([-100, 2, 5, -20, 2, 5, -1, 3]))
print(sys.maxsize)
y = 92233720368547758070
print(y)