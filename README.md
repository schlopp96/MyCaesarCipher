# MyCaesarCipher

> Simple cryptographic substitution-based cipher for encoding plaintext.

---

## About

- The [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher) is one of the most simple and well-known encryption techniques.

  - Each letter in the plaintext entry is replaced by a letter found a certain number of positions down the alphabet.

- This project was created as an exercise while I was taking the ["Cracking Codes with Python"](https://inventwithpython.com/cracking/) course - which I _highly_ recommend for both beginners and experienced python programmers interested in cryptography!

---

## Installation

### Using pip _(Recommended)_

> _Easiest_ method. _**Highly recommended**_ over manual installation.

- Run the following to install _**`MyCaesarCipher`**_ using `pip`:

```python
pip install MyCaesarCipher
```

- You should now be able to import/run _**`MyCaesarCipher`**_ within your python environment by entering the following:

```python
>>> from MyCaesarCipher import CaesarCipher
...
```

- Done!

---

### Manual Installation

> **_Not recommended._**

1. Before use, navigate to the intended installation location, and create a new directory.

2. Either clone repository with the git client of your preference, or download and extract the source code `zip` archive from the ["[releases"](https://github.com/schlopp96/MyCaesarCipher/releases) page to the newly created directory.

3. Install all dependencies for this package within said directory using:

   ```python
   pip install -r requirements.txt
   ```

   - (Optional) move the installation directory to **`"~Python/Libs/site_packages/"`** to be able to import this package to a Python environment like any other importable package.

- Done!

---

## Usage

- Within a Python environment or **`.py`** project, simply import the _**`MyCaesarCipher`**_ module to start encryption/decryption of ciphers.

### Message Encryption

- For encrypting text, use the **`CaesarCipher.encrypt`** class method:

```python
>>> from MyCaesarCipher import CaesarCipher

>>> cipher = CaesarCipher() # Create new class instance.
>>> msg = 'Test Cipher'
>>> encoder.encrypt(text=msg, key=200, print_to_console=True)

> Original Msg : Test Cipher
> Shift-Key : 200
> Encrypted Result: Lwkl Uahzwj
```

- Therefore the final encrypted result of "Test Cipher" using a shift-key of 200 is:
  - "**`LwklfUahzwj`**".

- Note that the `key: int` parameter is _optional_, and if not provided, a random key between 1 and 25 will be generated:

```python
>>> cipher.encrypt('Test Cipher', print_to_console=True)

> Original Msg : Test Cipher
> Shift-key : 19
> Encrypted Result: Mxlm Vbiaxk

>>> cipher.encrypt('Test Cipher', print_to_console=True)

> Original Msg : Test Cipher
> Shift-key : 24
> Encrypted Result: Rcqr Agnfcp

>>> cipher.encrypt('Test Cipher', print_to_console=True)

> Original Msg : Test Cipher
> Shift-key : 4
> Encrypted Result: Xiwx Gmtliv
```

---

### Message Decryption

- For decrypting text, use the **`CaesarCipher.decrypt`** class method:

```python
>>> from MyCaesarCipher import CaesarCipher

>>> cipher = CaesarCipher() # Create new class instance.
>>> code = 'Ozno Xdkczm'
>>> cipher.decrypt(text=code, print_to_console=True)

> Decrypted Shift-Key 0 : Ozno Xdkczm

> Decrypted Shift-Key 1 : Nymn Wcjbyl

> Decrypted Shift-Key 2 : Mxlm Vbiaxk

> Decrypted Shift-Key 3 : Lwkl Uahzwj

> Decrypted Shift-Key 4 : Kvjk Tzgyvi

> Decrypted Shift-Key 5 : Juij Syfxuh

> Decrypted Shift-Key 6 : Ithi Rxewtg

> Decrypted Shift-Key 7 : Hsgh Qwdvsf

> Decrypted Shift-Key 8 : Grfg Pvcure

> Decrypted Shift-Key 9 : Fqef Oubtqd

> Decrypted Shift-Key 10 : Epde Ntaspc

> Decrypted Shift-Key 11 : Docd Mszrob

> Decrypted Shift-Key 12 : Cnbc Lryqna

> Decrypted Shift-Key 13 : Bmab Kqxpmz

> Decrypted Shift-Key 14 : Alza Jpwoly

> Decrypted Shift-Key 15 : Zkyz Iovnkx

> Decrypted Shift-Key 16 : Yjxy Hnumjw

> Decrypted Shift-Key 17 : Xiwx Gmtliv

> Decrypted Shift-Key 18 : Whvw Flskhu

> Decrypted Shift-Key 19 : Vguv Ekrjgt

> Decrypted Shift-Key 20 : Uftu Djqifs

> Decrypted Shift-Key 21 : Test Cipher # <-- Correct Result

> Decrypted Shift-Key 22 : Sdrs Bhogdq

> Decrypted Shift-Key 23 : Rcqr Agnfcp

> Decrypted Shift-Key 24 : Qbpq Zfmebo

> Decrypted Shift-Key 25 : Paop Yeldan
```

- The **`CaesarCipher.decrypt`** method will return all possible shifted-key variations of the given encrypted message.

- _Generally_, the most legible key output will be the correct decrypted message, assuming the encrypted message was legible initially.

- Regardless, the correct output **MUST** be one of the output values due to the limitations of the algorithm being tied to the length of the alphabet 26 and the number of possible integers [0-9].

---

## Contact

- If you have any questions, comments, or concerns that cannot be alleviated through the [project's GitHub repository](https://github.com/schlopp96/MyCaesarCipher), please feel free to contact me through my email address:

  - `schloppdaddy@gmail.com`
