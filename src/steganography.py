def encode(text):
    """
    Encodes text into zero-width characters.
    0 -> \u200b (Zero Width Space)
    1 -> \u200c (Zero Width Non-Joiner)
    """
    binary = ''.join(format(ord(c), '08b') for c in text)
    encoded = binary.replace('0', '\u200b').replace('1', '\u200c')
    return encoded

def decode(text):
    """
    Decodes text from zero-width characters.
    Ignores non-zero-width characters.
    """
    binary = ''
    for char in text:
        if char == '\u200b':
            binary += '0'
        elif char == '\u200c':
            binary += '1'

    decoded = ''
    for i in range(0, len(binary), 8):
        byte = binary[i:i+8]
        if len(byte) == 8:
            decoded += chr(int(byte, 2))
    return decoded

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "encode" and len(sys.argv) > 2:
            print(encode(" ".join(sys.argv[2:])))
        elif command == "decode" and len(sys.argv) > 2:
            print(decode(" ".join(sys.argv[2:])))
