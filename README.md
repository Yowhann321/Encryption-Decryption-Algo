# Encryption-Decryption-Algo

A Python console program that encrypts and decrypts messages with four classical ciphers. It was built as our project for our Information Security course (IT129).

**[Try it in your browser →](https://yowhann321.github.io/MyPersonalWebsite/projects/cipher-lab/)** The web demo shows every step of the math.

## Ciphers

| # | Cipher | How it works |
|---|---|---|
| 1 | **Monoalphabetic** | Each letter (and digit) is swapped for another using a randomly shuffled key. Upper and lower case are kept. |
| 2 | **Vernam** | Letters become numbers (A=1 … Z=26) and are added to a repeating key word, wrapping past 26. Decryption subtracts the key. |
| 3 | **Kamasutra** | The alphabet is split into random letter pairs and each letter swaps with its partner, so the same step encrypts and decrypts. |
| 4 | **Kamasutra the Vernam** | Our own cipher: Vernam first, then a Kamasutra swap that also flips each letter's case. |

Keys for the substitution ciphers are generated fresh every time the program starts. Each cipher prints its key and explains its steps as it runs.

## Running it

You only need Python 3. No extra packages are required.

```
python MAIN_prog/MAIN_prog.py
```

Pick a cipher from the menu, then choose to encrypt or decrypt.

### Visual Studio

The project was made in Visual Studio 2022. To open it there, open `MAIN_prog.sln` (requires the Python development workload).

## Files

- `MAIN_prog/MAIN_prog.py`: the program, with a `CipherManager` menu that runs each cipher
- `MAIN_prog/MAIN_prog.pyproj` and `MAIN_prog.sln`: Visual Studio project files

The compiled `.exe` isn't included because Windows Defender flags it. Run the `.py` file with Python instead.
