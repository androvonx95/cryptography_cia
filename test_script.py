from solution import august_cipher, djb2_hash

def run_test(user_input):
    plaintext = user_input
    print(f"--- Round-Trip Test ---")
    
    # 1. Generate initial hash of plaintext
    initial_hash = djb2_hash(plaintext)
    
    # 2. Encrypt
    ciphertext = august_cipher(plaintext, mode='encrypt')
    
    # 3. Decrypt
    decrypted_text = august_cipher(ciphertext, mode='decrypt')
    
    # 4. Generate hash of decrypted result
    final_hash = djb2_hash(decrypted_text)
    
    print(f"Plaintext:  {plaintext}")
    print(f"Ciphertext: {ciphertext}")
    print(f"Decrypted:  {decrypted_text}")
    print(f"Hashes:     Initial({initial_hash}) == Final({final_hash})")
    
    if initial_hash == final_hash:
        print("VERIFICATION: SUCCESS")
    else:
        print("VERIFICATION: FAILED")

if __name__ == "__main__":
    user_input = input("Enter plaintext to test (Press Enter for default): ")
    if not user_input:
        user_input = "SHIV NADAR UNIVERSITY" # Default fallback
    run_test(user_input)