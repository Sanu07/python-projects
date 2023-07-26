def find_duplicate(nums_value) -> int:
    xor: int = 0
    for i in range(0, len(nums_value)):
        xor ^= nums_value[i]
    for i in range(1, len(nums_value)):
        xor ^= i

    return xor


if __name__ == '__main__':
    nums = [1, 2, 3, 4, 4]
    print(find_duplicate(nums))
