arr = [2, 4, 3, 1, 7, 8, 50, -1]

def minMax(arr):
    arr.sort()
    min = arr[0:(len(arr)-1)]
    max = arr[1:(len(arr))]
    summin = sum(min)
    summax = sum(max)

    print(f"{str(summin)} {str(summax)}")

minMax(arr)