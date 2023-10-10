def b2a_hex(s):
    result = []
    for char in s:
        c = (ord(char) >> 4) & 0xf
        if c > 9:
            c = c + ord('a') - 10
        else:
            c = c + ord('0')
        result.append(chr(c))
        c = ord(char) & 0xf
        if c > 9:
            c = c + ord('a') - 10
        else:
            c = c + ord('0')
        result.append(chr(c))
    return ''.join(result)

hexlify = b2a_hex


table_hex = [
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    0, 1, 2, 3,  4, 5, 6, 7,  8, 9,-1,-1, -1,-1,-1,-1,
    -1,10,11,12, 13,14,15,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,10,11,12, 13,14,15,-1, -1,-1,-1,-1, -1,-1,-1,-1,
    -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1, -1,-1,-1,-1
]


def a2b_hex(t):
    result = []

    def pairs_gen(s):
        while s:
            try:
                yield table_hex[ord(s[0])], table_hex[ord(s[1])]
            except IndexError:
                if len(s):
                    raise TypeError('Odd-length string')
                return
            s = s[2:]

    for a, b in pairs_gen(t):
        if a < 0 or b < 0:
            raise TypeError('Non-hexadecimal digit found')
        result.append(chr((a << 4) + b))
    return bytes(''.join(result))
    
unhexlify = a2b_hex
