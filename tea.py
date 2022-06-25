def decrypt(v):
    v6 = bytes_to_long(long_to_bytes(v[0])[::-1])
    v9 = bytes_to_long(long_to_bytes(v[1])[::-1])
    #v6 = v[0]
    #v9 = v[1]
    delta = 0
    for _ in range(32):
        delta = (delta - 0x61C88647) & 0xFFFFFFFF
    for _ in range(32):
        v9 -= (16 * v6 + 12) ^ ((v6 >> 5) + 25) ^ (v6 + delta)
        v9 &= 0xFFFFFFFF
        v6 -= (v9 >> 5) ^ (16 * v9 + 20) ^ (v9 + delta)
        v6 &= 0xFFFFFFFF
        delta += 0x61C88647
        delta &= 0xFFFFFFFF
    v[0] = v6
    v[1] = v9
    return v
