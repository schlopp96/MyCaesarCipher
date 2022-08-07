from typing import Any
from MyCaesarCipher.mycaesarcipher import CaesarCipher


class CaesarCipherTesting:

    def __init__(self, test_class=CaesarCipher()) -> None:
        self.test_class: Any = test_class

    def test_encrypt(
        self,
        text,
        key,
        assertion,
        output_results: bool = True,
    ) -> None:
        assert self.test_class.encrypt(text, key, output_results) == assertion

    def test_decrypt(self,
                     text,
                     assertion,
                     output_results: bool = False) -> None:
        assert self.test_class.decrypt(text, output_results) == assertion


testCC: CaesarCipherTesting = CaesarCipherTesting()


def test_encodeA() -> None:
    testCC.test_encrypt('TESTING', 5, 'YJXYNSL')


def test_encodeB() -> None:
    testCC.test_encrypt("TeStInG", 5, 'YjXyNsL', False)


def test_encodeC() -> None:
    testCC.test_encrypt("Kk", 5, 'Pp', False)


def test_encodeD() -> None:
    testCC.test_encrypt("Password", 5, 'Ufxxbtwi', False)


def test_decodeA() -> None:
    testCC.test_decrypt('YJXYNSL', 'ZKYZOTM')


def test_decodeB() -> None:
    testCC.test_decrypt('YjXyNsL', 'ZkYzOtM', False)


def test_decodeC() -> None:
    testCC.test_decrypt('1djjktcqttccwprztsd', '2ekkludruuddxqsaute')
