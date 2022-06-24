
arr = [-4, -3, 2, 0, 0, 1, -2]

def plusMinus(arr):
    zeros = 0
    positives = 0
    negatives = 0
    for i in arr:
        if i == 0:
            zeros += 1
        elif i > 0:
            positives += 1
        elif i < 0:
            negatives += 1
    zero_ratio = zeros/(len(arr))
    pos_ratio = positives/(len(arr))
    neg_ratio = negatives/(len(arr))

    print("{0:.6f}".format(zero_ratio))
    print("{0:.6f}".format(pos_ratio))
    print("{0:.6f}".format(neg_ratio))
plusMinus(arr)