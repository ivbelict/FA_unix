def encrypt(k, m):

    encrypted = ""

    for c in k:

        if c.isupper():
            c_index = ord(c) - ord('A')
            c_shifted = (c_index + m) % 26 + ord('A')
            c_new = chr(c_shifted)
            encrypted += c_new

        elif c.islower():
            c_index = ord(c) - ord('a')

            c_shifted = (c_index + m) % 26 + ord('a')

            c_new = chr(c_shifted)

            encrypted += c_new

        elif c.isdigit():
            c_new = (int(c) + m) % 10
            encrypted += str(c_new)
        else:
            encrypted += c

    return encrypted

def decrypt(k, c):

    decrypted = ""

    for c in k:

        if c.isupper():
            c_index = ord(c) - ord('A')
            c_og_pos = (c_index - c) % 26 + ord('A')
            c_og = chr(c_og_pos)
            decrypted += c_og

        elif c.islower():
            c_index = ord(c) - ord('a')
            c_og_pos = (c_index - c) % 26 + ord('a')
            c_og = chr(c_og_pos)
            decrypted += c_og

        elif c.isdigit():
            c_og = (int(c) - c) % 10

            decrypted += str(c_og)

        else:
            decrypted += c

    return decrypted



def vigenere_encrypt(text, keys):
    n = len(keys)
    translatedText = ""

    i = 0

    for c in text:

        if c.islower():

            shift = keys[i % n]

            shifted_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            translatedText += shifted_c
            i += 1
        else:
            translatedText += c

    return translatedText



def vigenere_decrypt(text, keys):
    n = len(keys)
    translatedText = ""

    i = 0

    for c in text:

        if c.islower():

            shift = keys[i % n]
            shift = -shift

            shifted_c = chr((ord(c) - ord('a') + shift) % 26 + ord('a'))
            translatedText += shifted_c
            i += 1
        else:
            translatedText += c

    return translatedText