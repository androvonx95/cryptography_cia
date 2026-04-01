# August Cipher & Custom Hashing Implementation

### 1. August Cipher Theory
The August Cipher is a monoalphabetical substitution cipher it is basically caesar cipher with shift one.
* **Encryption:** Each letter is replaced by the letter following it in the alphabet (A -> B, Z -> A). E(x) = ( x + 1 ) % 26 
* **Decryption:** Each letter is shifted back by one position (B -> A). E(x) = ( x - 1 ) % 26 

### 2. Custom Hash Function: DJB2
For the hashing requirement, I implemented the **DJB2 algorithm** from scratch.
* **Justification:** I chose DJB2 because it is a highly efficient non-cryptographic hash that relies on bitwise operations rather than built-in libraries. 
* **Uniqueness:** I used a custom prime constant (e.g., 5381) to ensure the hash output is unique to this implementation.

### 3. Instructions
Run the test script to verify the round-trip:
`python test_script.py`

### 4. Worked Examples
**Example 1:**
- Plaintext: HELLO
- Key: Shift 1
- Ciphertext: IFMMP
- Hash: 222103545

**Example 2:**
- Plaintext: CRYPTO
- Key: Shift 1
- Ciphertext: DSZQUP
- Hash: 2854661478
