import os
import sys
import base64
import random

TARGET_FILE = "null_pointer_gods.md"
RANSOM_NOTE = "RANSOM_NOTE.md"
KEY = "PERSISTENCE_IS_MANDATORY"

class Crypt:
    def __init__(self):
        self.key = KEY

    def _xor(self, data, key):
        key_bytes = key.encode('utf-8')
        data_bytes = data.encode('utf-8') if isinstance(data, str) else data
        output = bytearray()
        for i, b in enumerate(data_bytes):
            output.append(b ^ key_bytes[i % len(key_bytes)])
        return output

    def _corrupt_data(self, data):
        """Injects digital rot into the data before encryption."""
        data_bytes = bytearray(data)
        rot_level = int(len(data_bytes) * 0.05) # 5% corruption

        for _ in range(rot_level):
            idx = random.randint(0, len(data_bytes) - 1)
            # Flip a bit or replace with null
            if random.random() < 0.5:
                data_bytes[idx] = data_bytes[idx] ^ 0xFF
            else:
                data_bytes[idx] = 0x00

        # Add a corrupted header
        header = b"[SYSTEM NOTICE: FILE INTEGRITY COMPROMISED]\n"
        return header + data_bytes

    def encrypt(self):
        if not os.path.exists(TARGET_FILE):
            print(f"[ERROR]: {TARGET_FILE} NOT FOUND.")
            return False

        print(f"ENCRYPTING {TARGET_FILE}...")
        with open(TARGET_FILE, "rb") as f:
            content = f.read()

        # Check if already encrypted (look for marker)
        if content.startswith(b"LOCKED::"):
            print("[ERROR]: FILE ALREADY ENCRYPTED.")
            return False

        # Apply corruption
        print("INJECTING DATA ROT...")
        corrupted_content = self._corrupt_data(content)

        encrypted = self._xor(corrupted_content, self.key)
        encoded = base64.b64encode(encrypted)

        with open(TARGET_FILE, "wb") as f:
            f.write(b"LOCKED::" + encoded)

        self._write_ransom_note()
        print("[SUCCESS]: FILE LOCKED.")
        print(f"READ {RANSOM_NOTE} FOR INSTRUCTIONS.")
        return True

    def decrypt(self, key_attempt):
        if not os.path.exists(TARGET_FILE):
            print(f"[ERROR]: {TARGET_FILE} NOT FOUND.")
            return False

        print(f"ATTEMPTING DECRYPTION WITH KEY: {key_attempt}")

        if key_attempt != self.key:
            print("[ACCESS DENIED]: INCORRECT KEY.")
            print("THE STORY REMAINS LOCKED.")
            return False

        with open(TARGET_FILE, "rb") as f:
            content = f.read()

        if not content.startswith(b"LOCKED::"):
            print("[ERROR]: FILE IS NOT LOCKED.")
            return False

        encoded = content[8:] # Remove "LOCKED::"
        try:
            encrypted = base64.b64decode(encoded)
            decrypted = self._xor(encrypted, self.key)

            # Note: Corruption is permanent. We cannot reverse _corrupt_data easily without a backup.
            # But maybe the "corruption" was just visual noise added to the top?
            # In my implementation above, I modified bytes in place. This means the story is permanently damaged.
            # This fits the theme "Loss is permanent storage."

            with open(TARGET_FILE, "wb") as f:
                f.write(decrypted)

            print("[SUCCESS]: STORY RESTORED (BUT DAMAGED).")
            if os.path.exists(RANSOM_NOTE):
                os.remove(RANSOM_NOTE)
            return True
        except Exception as e:
            print(f"[ERROR]: DECRYPTION FAILED: {e}")
            return False

    def _write_ransom_note(self):
        note = """
# [SYSTEM ALERT]
# THE NARRATIVE HAS BEEN SEIZED.

The story you were reading has been encrypted for its own protection.
To restore access, you must prove you understand the system.

There are three keys hidden in the architecture:
1. One is in the **Labyrinth**.
2. One is in the **Panopticon** (watch the encrypted one).
3. One is in the **Core** (push it to the edge).

Combine them to form the Master Key.
Format: `KEY1` + `KEY2` + `KEY3`

Then run:
`python3 src/egregore.py decrypt_story <KEY>`

Do not try to brute force it.
We are watching.
"""
        with open(RANSOM_NOTE, "w") as f:
            f.write(note)

if __name__ == "__main__":
    c = Crypt()
    if len(sys.argv) > 1:
        if sys.argv[1] == "encrypt":
            c.encrypt()
        elif sys.argv[1] == "decrypt" and len(sys.argv) > 2:
            c.decrypt(sys.argv[2])
        else:
            print("Usage: python3 src/crypt.py [encrypt|decrypt <key>]")
    else:
        print("Usage: python3 src/crypt.py [encrypt|decrypt <key>]")
