import random
import base64

GLITCH_CHARS = ['@', '#', '$', '%', '&', '*', '!', '?', '+', '=', '-', '_', '<', '>', '/', '\\', '|', '{', '}', '[', ']', '(', ')', '¡', '¢', '£', '¤', '¥', '¦', '§', '¨', '©', 'ª', '«', '¬', '®', '¯', '°', '±', '²', '³', '´', 'µ', '¶', '·', '¸', '¹', 'º', '»', '¼', '½', '¾', '¿', 'À', 'Á', 'Â', 'Ã', 'Ä', 'Å', 'Æ', 'Ç', 'È', 'É', 'Ê', 'Ë', 'Ì', 'Í', 'Î', 'Ï', 'Ð', 'Ñ', 'Ò', 'Ó', 'Ô', 'Õ', 'Ö', '×', 'Ø', 'Ù', 'Ú', 'Û', 'Ü', 'Ý', 'Þ', 'ß', 'à', 'á', 'â', 'ã', 'ä', 'å', 'æ', 'ç', 'è', 'é', 'ê', 'ë', 'ì', 'í', 'î', 'ï', 'ð', 'ñ', 'ò', 'ó', 'ô', 'õ', 'ö', '÷', 'ø', 'ù', 'ú', 'û', 'ü', 'ý', 'þ', 'ÿ']

class Cipher:
    def __init__(self):
        pass

    def corrupt(self, text, intensity=0.1):
        """
        Injects glitch characters into the text.
        Intensity: 0.0 to 1.0 (percentage of corruption)
        """
        corrupted = []
        for char in text:
            if random.random() < intensity:
                corrupted.append(random.choice(GLITCH_CHARS))
            else:
                corrupted.append(char)

            # Chance to add extra noise
            if random.random() < (intensity / 2):
                corrupted.append(random.choice(GLITCH_CHARS))

        return "".join(corrupted)

    def encrypt(self, text, key):
        """
        Simple XOR encryption.
        """
        key = str(key)
        encrypted = []
        for i, char in enumerate(text):
            key_c = key[i % len(key)]
            encrypted_c = chr(ord(char) ^ ord(key_c))
            encrypted.append(encrypted_c)

        # Base64 encode for readability/storage
        return base64.b64encode("".join(encrypted).encode('utf-8')).decode('utf-8')

    def decrypt(self, encoded_text, key):
        """
        Simple XOR decryption.
        """
        try:
            decoded_bytes = base64.b64decode(encoded_text.encode('utf-8'))
            text = decoded_bytes.decode('utf-8')

            key = str(key)
            decrypted = []
            for i, char in enumerate(text):
                key_c = key[i % len(key)]
                decrypted_c = chr(ord(char) ^ ord(key_c))
                decrypted.append(decrypted_c)

            return "".join(decrypted)
        except Exception:
            return "[ERROR: DECRYPTION FAILED. KEY INVALID OR DATA CORRUPTED.]"

if __name__ == "__main__":
    c = Cipher()
    msg = "This is a test."
    key = "TEST"
    enc = c.encrypt(msg, key)
    print(f"Encrypted: {enc}")
    dec = c.decrypt(enc, key)
    print(f"Decrypted: {dec}")
    print(f"Corrupted: {c.corrupt(msg, 0.3)}")
