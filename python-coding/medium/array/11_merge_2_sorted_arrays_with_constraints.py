# Given two sorted arrays X[] and Y[] of size m and n each where m >= n
# and X[] has exactly n vacant cells, merge elements of Y[] in
# their correct position in array X[], i.e., merge (X, Y) by keeping the sorted order.
#
# Input:
#
# X[] = {0, 2, 0, 3, 0, 5, 6, 0, 0}
# Y[] = {1, 8, 9, 10, 15}
#
# The vacant cells in X[] is represented by 0
#
# Output:
#
# X[] = {1, 2, 3, 5, 6, 8, 9, 10, 15}

def merge_y_into_x(x: [int], y: [int]):
    j: int = 0
    k: int = 0

    for i in range(0, len(x)):
        while (i < len(x)) and x[i] != 0:
            i += 1

        j = i

        while j < len(x) and not (x[j] > 0):
            j += 1

        if j >= len(x):
            while i < len(x):
                x[i] = y[k]
                i += 1
                k += 1
            break

        if x[j] > y[k]:
            x[i] = y[k]
            k += 1
        else:
            x[i] = x[j]
            x[j] = 0


if __name__ == '__main__':
    x = [0, 2, 0, 3, 0, 5, 6, 0, 0]
    merge_y_into_x(x, y=[1, 8, 9, 10, 15])
    print(x)
