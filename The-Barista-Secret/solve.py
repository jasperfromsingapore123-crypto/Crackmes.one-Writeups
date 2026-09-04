mask = 0xFFFFFFFF
def rol32(x, n):
    x &= mask
    return ((x << n) | (x >> (32 - n))) & mask

def brewhash(data, length):
    result = 0xC0FFEE42
    for byte in data:
        result ^= byte * 0x9E3779B1
        result &= mask
        result = rol32(result, 13)
        result -= 0x3F001200
        result &= mask
    return result

def check1(A, B):
    return B == (A ^ 0xC0FFEE42)

def check2(C):
    a = b"espresso"
    b = b"arabica"
    part1 = (
        a[3] << 24 |
        a[1] << 8 |
        a[0] |
        a[2] << 16
    )
    part2 = (
        a[7] << 24 |
        a[5] << 8 |
        a[4] |
        a[6] << 16
    )
    first_part = C ^ part1 ^ part2
    part3 = (
        b[3] << 24 |
        b[1] << 8 |
        b[0] |
        b[2] << 16
    )

    return (first_part ^ part3) == 0xCAFEBABE


def check3(A, B):
    data = [0] * 8
    for i in range(4):
        data[i] = (A >> (i * 8)) & 0xFF
    for i in range(4):
        data[i + 4] = (B >> (i * 8)) & 0xFF
    return (brewhash(data, 8) & 0xFFFFF) == 0xDECAF

def solve_c():
    # Reverse check2
    a = b"espresso"
    b = b"arabica"
    part1 = (
        a[3] << 24 |
        a[1] << 8 |
        a[0] |
        a[2] << 16
    )
    part2 = (
        a[7] << 24 |
        a[5] << 8 |
        a[4] |
        a[6] << 16
    )
    part3 = (
        b[3] << 24 |
        b[1] << 8 |
        b[0] |
        b[2] << 16
    )
    C = 0xCAFEBABE ^ part1 ^ part2 ^ part3
    return C & mask


c = solve_c()

print(f"[*] C = {c:08X}")
print(f"[*] check2(c) = {check2(c)}")
print("[*] Searching for A")
for a in range(0x100000000):
    b = a ^ 0xC0FFEE42
    if check1(a, b) and check3(a, b):
        print("Flag found!!!")
        serial = f"BREW-{a:08X}-{b:08X}-{c:08X}"
        print(f"Serial: {serial}")
        print(f"Flag: CODEBREW{{{serial[5:]}}}")
        break
