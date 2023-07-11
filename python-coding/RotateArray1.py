class RotateArray:
    def __int__(self):
        pass

    @staticmethod
    def swap_array(arr, i, j):
        while i <= j:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            i += 1
            j -= 1

    def rotate_array_reverse(self, arr, k):
        k = k % len(arr)
        self.swap_array(arr, 0, len(arr) - k - 1)
        self.swap_array(arr, len(arr) - k, len(arr) - 1)
        self.swap_array(arr, 0, len(arr) - 1)
        print(arr)


result = RotateArray()
result.rotate_array_reverse(arr=[1, 2, 3, 4, 5, 6, 7], k=3)




