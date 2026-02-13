import random
import time
import sys

class BioCipher:
    def __init__(self):
        self.bases = ['A', 'T', 'C', 'G']
        self.key = "BLOOD" # Default key, can be overridden

    def encrypt(self, text):
        encrypted = ""
        for char in text:
            # Convert char to binary
            binary = format(ord(char), '08b')
            # Convert binary to DNA bases: 0 -> A/T, 1 -> C/G
            dna = ""
            for bit in binary:
                if bit == '0':
                    dna += random.choice(['A', 'T'])
                else:
                    dna += random.choice(['C', 'G'])
            encrypted += dna + "-"
        return encrypted[:-1]

    def decrypt(self, text, key):
        # Simulate bio-verification delay
        # Only print if running as main or if verbose is needed, but for library usage, maybe suppress or return status?
        # Let's keep it simple for now.

        if key.upper() != self.key:
            return "[ERROR: DNA MISMATCH. SAMPLE REJECTED.]"

        decrypted = ""
        segments = text.split("-")
        for segment in segments:
            binary = ""
            for base in segment:
                if base in ['A', 'T']:
                    binary += '0'
                elif base in ['C', 'G']:
                    binary += '1'

            # Simulate occasional mutation/error during decryption
            if random.random() < 0.05:
                # Flip a bit
                if len(binary) > 0:
                    binary_list = list(binary)
                    idx = random.randint(0, len(binary_list)-1)
                    binary_list[idx] = '1' if binary_list[idx] == '0' else '0'
                    binary = "".join(binary_list)

            if len(binary) == 8:
                try:
                    decrypted += chr(int(binary, 2))
                except ValueError:
                    decrypted += "?"
            else:
                decrypted += "?"
        return decrypted

if __name__ == "__main__":
    cipher = BioCipher()
    if len(sys.argv) > 1:
        command = sys.argv[1]
        if command == "encrypt" and len(sys.argv) > 2:
            print(cipher.encrypt(" ".join(sys.argv[2:])))
        elif command == "decrypt" and len(sys.argv) > 3:
            # decrypt <key> <text>
            key = sys.argv[2]
            text = " ".join(sys.argv[3:])
            print(cipher.decrypt(text, key))
        else:
            print("Usage: python src/cipher.py [encrypt|decrypt] [key for decrypt] [text]")
    else:
        # Test
        test_text = "HELLO WORLD"
        encrypted = cipher.encrypt(test_text)
        print(f"Encrypted: {encrypted}")
        decrypted = cipher.decrypt(encrypted, "BLOOD")
        print(f"Decrypted: {decrypted}")
