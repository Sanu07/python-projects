# /**
#  *
#  * Given two sorted arrays, X[] and Y[] of size m and n each, merge elements of X[] with elements of array Y[]
#  * by maintaining the sorted order, i.e., fill X[] with the first m smallest elements and fill Y[]
#  * with remaining elements.
#  *
#  * Do the conversion in-place and without using any other data structure.
#  *
#  * Input:
#  *
#  * X[] = { 1, 4, 7, 8, 10 }
#  * Y[] = { 2, 3, 9 }
#  *
#  * Output:
#  *
#  * X[] = { 1, 2, 3, 4, 7 }
#  * Y[] = { 8, 9, 10 }
#  *
#  */

def swap(x: [int], y: [int], x_i: int, y_i: int):
    temp: int = x[x_i]
    x[x_i] = y[y_i]
    y[y_i] = temp


def merge_sorted_arrays(x: [int], y: [int]):
    for i in range(0, len(x)):
        if x[i] > y[0]:
            swap(x, y, i, 0)

        for j in range(0, len(y) - 1):
            if y[j] > y[j + 1]:
                temp: int = y[j]
                y[j] = y[j + 1]
                y[j + 1] = temp


if __name__ == '__main__':
    x: [int] = [1, 4, 7, 8, 10]
    y: [int] = [2, 3, 9]
    merge_sorted_arrays(x, y)
    print(x)
    print(y)
