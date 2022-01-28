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

    def _transform(self, original, code):
        msg = list(original)
        for i in range(len(msg)):
            if msg[i].isupper():
                j = ord(msg[k]) - ord("A")
                msg[i] = code[j]
        return "".join(msg)

    if __name__ == '__main__':
        cipher = CeasarCipher(3)
        message = "THE EAGLE IS IN PLAY; MEET AT JOE'S"
        coded = cipher.encrypt(message)
        print('Secret: ', coded)
        answer = cipher.decrypt(coded)
        print('Message: ', answer)
