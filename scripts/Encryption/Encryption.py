from abc import ABC,abstractmethod
class Encryption(ABC):
    @abstractmethod
    def encrypt(self, plaintext):
        pass

    @abstractmethod
    def decrypt(self, ciphertext):
        pass

class CaesarCipher(Encryption):
    def __init__(self, shift):
        self.shift = shift % 26

    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                ascii_offset = ord('A')
                if char.islower():
                    ascii_offset = ord('a')
                encrypted_char = chr((ord(char) - ascii_offset + self.shift) % 26 + ascii_offset)
                ciphertext += encrypted_char
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        plaintext = ''
        for char in ciphertext:
            if char.isalpha():
                ascii_offset = ord('A')
                if char.islower():
                    ascii_offset = ord('a')
                decrypted_char = chr((ord(char) - ascii_offset - self.shift) % 26 + ascii_offset)
                plaintext += decrypted_char
            else:
                plaintext += char
        return plaintext

class ROT13Cipher(Encryption):
    def encrypt(self, plaintext):
        ciphertext = ''
        for char in plaintext:
            if char.isalpha():
                ascii_offset = ord('A') if char.isupper() else ord('a')
                rotated_char = chr((ord(char) - ascii_offset + 13) % 26 + ascii_offset)
                ciphertext += rotated_char
            else:
                ciphertext += char
        return ciphertext

    def decrypt(self, ciphertext):
        return self.encrypt(ciphertext)