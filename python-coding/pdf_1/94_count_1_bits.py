class Count1Bits:

    def __init__(self):
        pass

    def count_bits(self):
        num = 11 # 1011
        count = 0
        for i in range(0, 33):
            if (num & (1 << i)) != 0:
                count += 1
        print(count)


res = Count1Bits()
res.count_bits()