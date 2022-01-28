class CeasarCipher:

    def __init__(self, shift):
        encoder = [None] * 26
        decoder = [None] * 26
        for i in range(26):
            encoder[i] = chr((i + shift) % 26 + ord("A"))
            decoder[i] = chr((i - shift) % 26 + ord("A"))
        self._forward = "".join(encoder)
        self._backward = "".join(decoder)

    def encrypt(self, message):
        return self._transform(message, self._forward)

    def decrypt(self, secret):
        return self._transform(self, self._backward)
