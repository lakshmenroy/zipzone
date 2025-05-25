def text_to_binary(text: str) -> bytes:
    """Convert text to binary string for storage."""
    binary = ""
    for char in text:
        binary += format(ord(char), '08b')
    return int(binary, 2).to_bytes((len(binary) + 7) // 8, 'big')

def binary_to_text(binary: bytes) -> str:
    """Convert binary string back to text."""
    binary_str = ''.join(format(byte, '08b') for byte in binary)
    chars = []
    for i in range(0, len(binary_str), 8):
        byte = binary_str[i:i+8]
        if len(byte) == 8:
            chars.append(chr(int(byte, 2)))
    return ''.join(chars)