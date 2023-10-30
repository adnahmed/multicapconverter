"""Return the hexadecimal representation of the binary data. 
Every byte of data is converted into the corresponding 2-digit hex representation. 
The resulting string is therefore twice as long as the length of data."""
"Example:"
"> hexlify('ad')"
'6164'

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

"""Return the hexadecimal representation of the binary data.
Every byte of data is converted into the corresponding 2-digit hex representation.
The resulting string is therefore twice as long as the length of data."""
"Example:"
"> unhexlify('6164')"
'ad'

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
    return bytes(''.join(result), encoding='utf-8')
    
unhexlify = a2b_hex

"fromhex($type, string, /)\n"
"Create a bytes object from a string of hexadecimal numbers.\n"
"Spaces between two numbers are accepted.\n"
"Example: bytes.fromhex(\'B9 01EF\') -> b\'\\\\xb9\\\\x01\\\\xef\'."

def fromhex(_hex): 
    if len(_hex) == 0:
        raise ValueError('Error: Empty Hex value.')
    _hex = _hex.replace(' ', '')
    if len(_hex) % 2 != 0 :
        raise ValueError('Error: Hex value has odd length.')
    _bytes = []
    i = 0
    while i < len(_hex):
        v = _hex[i] + _hex[i + 1]
        _bytes.append(int(v, 16))
        i += 2
    __pragma__ ('js', '{}', 'return Uint8Array.from(_bytes)')


"Example:\n"
">>> value = b\'\\xb9\\x01\\xef\'\n"
">>> value.hex()\n"
"\'b901ef\'\n"
">>> value.hex(\':\')\n"
"\'b9:01:ef\'\n"
">>> value.hex(\':\', 2)\n"
"\'b9:01ef\'\n"
">>> value.hex(\':\', -2)\n"
"\'b901:ef\'"

def hex(bytes):
	return ''.join('{:02x}'.format(a) for a in [b for b in bytes])