#!/usr/bin/env python3

from random import randint


class CaesarCipher:
    """Cryptographic encryption/decryption techniques using the Caesar-Cipher algorithm.

    ---

    - Substitutes each letter of a message with new "matching" letter shifted down alphabetically by a given amount.

    - Not intended for real-world cryptographic applications, as the Caesar-Cipher algorithm is notoriously easy to crack.

    - More information on this cipher:
        - https://en.wikipedia.org/wiki/Caesar_cipher
    """

    @staticmethod
    def encrypt(text: str, key: int = None, stdout_output: bool = True) -> str:
        """Encrypt text using the Caesar-Cypher cryptography algorithm.

        - Generates encrypted form of :param:`text` using the Caesar-Cipher algorithm.
        - If no :param:`key` is provided, a random integer value is generated.

        :param text: text to encrypt.
        :type text: :class:`str`
        :param key: numeric value used to encrypt the given text, defaults to `None`
        :type key: :class:`int`, optional
        :param stdout_output: toggle output to stdout, defaults to `True`
        :type stdout_output: :class:`bool`, optional
        :return: encrypted form of :param:`text`
        :rtype: :class:`str`
        """

        result: str = ''

        if key is None:
            key = randint(1, 25)

        #@ Iterate through text char by char.
        for character in text:

            #@ Encrypt uppercase characters in text
            if (character.isupper()):
                result += chr((ord(character) + key - 65) % 26 + 65)

            #@ Encrypt lowercase characters in text
            elif (character.islower()):
                result += chr((ord(character) + key - 97) % 26 + 97)

            #@ Encrypt numbers in text
            elif (character.isdigit()):
                result += str((int(character) + key) % 10)

            #@ Leave all non-alphanumeric characters unchanged.
            else:
                result += character

        info: str = f'> Original Msg : {text}\n> Shift-key : {key}\n> Encrypted Result: {result}\n'

        if stdout_output:
            print(info)

        return result

    @staticmethod
    def decrypt(text: str, stdout_output: bool = True):
        """Decrypt Caesar-Cipher encrypted messages using brute force.

        ---

        :param text: text to decode.
        :type text: :class:`str`
        :param stdout_output: toggle output to stdout, defaults to `True`.
        :type stdout_output: :class:`bool`
        :return: all possible pairs of shift-keys and their decrypted results.
        :rtype: :class:`str`
        """

        translated = ''

        #@ Outputs all possible shift-keys using the english alphabet.
        for key in range(26):

            for character in text:

                if (character.isupper()):
                    translated += chr((ord(character) - key - 65) % 26 + 65)

                #@ Decrypt lowercase characters in text
                elif (character.islower()):
                    translated += chr((ord(character) - key - 97) % 26 + 97)

                #@ Decrypt numbers in text
                elif (character.isdigit()):
                    translated += str((int(character) - key) % 10)

                #@ Leave all non-alphanumeric characters unchanged.
                else:
                    translated += character

            if stdout_output:
                print(f'> Decrypted Shift-Key {key} : {translated}\n')

        return translated