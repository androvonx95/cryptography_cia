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

# --- The Test Script Round-Trip ---
plaintext = "SNU CHENNAI"
h1 = djb2_hash(plaintext)
ciphertext = august_cipher(plaintext, 'encrypt')
decrypted = august_cipher(ciphertext, 'decrypt')
h2 = djb2_hash(decrypted)

print(f"Original: {plaintext} (Hash: {h1})")
print(f"Ciphertext: {ciphertext}")
print(f"Decrypted: {decrypted} (Hash: {h2})")
print("Verification:", "SUCCESS" if h1 == h2 else "FAILED")
