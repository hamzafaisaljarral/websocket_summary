import time


def oneminsummary(b):
    struct = {}
    prime_num = []
    even_num = []
    odd_num = []
    struct["max"] = max(b)
    # find the min in b
    struct["min"] = min(b)
    # find the first in b
    struct["first"] = b[0]
    # find the last in b
    struct["last"] = b[-1]
    # find the number of prime numbers

    for i in b:
        c = 0
        for j in range(1, i):
            if i % j == 0:
                c += 1
        if c == 1:
            prime_num.append(i)
        if i % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)
    struct["prime"] = prime_num
    struct["even_number"] = even_num
    struct["odd_number"] = odd_num

    time.sleep(1)
    print(struct)
    return struct