def august_cipher(text, mode='encrypt'):
    result = ""
    shift = 1 if mode == 'encrypt' else -1
    for char in text.upper():
        if char.isalpha():
            # Shift by 1 (A=0, Z=25)
            stay_in_alphabet = (ord(char) - ord('A') + shift) % 26
            result += chr(stay_in_alphabet + ord('A'))
        else:
            result += char
    return result

def djb2_hash(string):
    # Using 5381 as the magic constant
    hash_val = 5381
    for char in string:
        # hash * 33 + char
        hash_val = ((hash_val << 5) + hash_val) + ord(char)
    return hash_val & 0xFFFFFFFF  # Keep it to 32-bit for clean output