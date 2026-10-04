import importlib
import sys
import os

from sre_parse import parse_template

import string
import random


class CipherManager:
    def __init__(self):
        self.ciphers = {
            "1": {
                "name": "Monoalphabetic Cipher",
                "module": {"name": "mono", "func": run_mono},
                "description": "The Monoalphabetic Cipher is a simple substitution cipher where each letter in the plaintext is replaced with another letter from a fixed key mapping. It has been used historically in various forms, including the Caesar cipher, though it is vulnerable to frequency analysis.",
            },
            "2": {
                "name": "Vernam Cipher",
                "module": {"name": "vernam", "func": run_vernam},
                "description": "The Vernam Cipher, also known as the One-Time Pad, is an encryption technique that is theoretically unbreakable when used correctly. It was invented in 1917 by Gilbert Vernam and uses a key that is as long as the message, consisting of completely random characters.",
            },
            "3": {
                "name": "Kamasutra Cipher",
                "module": {"name": "Kamasutra", "func": run_kamasutra},
                "description": "The Kamasutra Cipher is a monoalphabetic substitution cipher that swaps letter pairs randomly to create an encryption scheme. It is named after the ancient Indian text but has no historical relation to it. The encryption key changes each time it is used.",
            },
            "4": {
                "name": "Custom Cipher (Kamasutra the Vernam)",
                "module": {"name": "Custom_cipher", "func": run_custom_cipher},
                "description": "The Custom Cipher combines elements of the Vernam and Kamasutra ciphers. It applies Vernam's key-based transformation along with Kamasutra's letter pairing mechanism. Additionally, it has special features, such as case-reversal.",
            },
        }

    def display_menu(self):
        print("\n===== Cipher Selection Menu =====")
        print("Please select a cipher to use:")
        for key, value in self.ciphers.items():
            print(f"{key} - {value['name']}")
        print("5 - Exit")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nEnter your choice: ")

            if choice == "5":
                print("Goodbye!")
                break

            if choice in self.ciphers:
                self.display_cipher_info(self.ciphers[choice])
                input("\nPress Enter to continue...")
                self.run_cipher(self.ciphers[choice]["module"])
            else:
                print("Invalid choice. Please try again.")

    def display_cipher_info(self, cipher):
        os.system("cls" if os.name == "nt" else "clear")
        print(f"\n===== {cipher['name']} =====")
        print(cipher["description"])
        print("\n")

    def run_cipher(self, module):
        try:
            # cipher_module = importlib.import_module(module_name)
            os.system("cls" if os.name == "nt" else "clear")
            print(f"\n===== Running {module['name']}.py =====\n")
            module["func"]()
            input("\nPress Enter to return to the main menu...")
            os.system("cls" if os.name == "nt" else "clear")
        except ImportError:
            print(f"Error: Could not import module '{module['name']}'.")
            print("Make sure the file exists in the same directory.")
        except AttributeError:
            print(
                f"Error: The module '{module['name']}' does not have a main() function."
            )
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")


def run_kamasutra():
    ## Creates the list of letters of the Alphabet
    letters = string.ascii_lowercase
    ##Creates emmpty list to contain two groups of letters
    set1 = []
    set2 = []
    ##Empty dictionaries to be containers for the key
    dict_let = {}
    rev_dict = {}

    ##The function that creates the key
    def key_create():
        ##This for loop separates the letters, with every other letter going to the set2 list
        for i, let in zip(range(0, 26), letters):
            if i % 2 == 1:
                set1.append(letters[i])
            else:
                set2.append(letters[i])
        ##This just shuffles both lists of letters to make it more random
        random.shuffle(set1)
        random.shuffle(set2)
        ##This takes the letters from both lists, and forms them into a dictionary
        ## the rev_dict is a reverse dictionary of the dict_let since in the kamasutra cipher
        ## The plaintext is also the key and vice versa
        for j, k in zip(set1, set2):
            dict_let[j] = k
            rev_dict[k] = j

    ##This is the function that processess the string input
    ##Again, since in kamasutra, the plaintext is also the key, the same process could be applied for encrypting and decyrpting
    def process(text):
        processed = ""
        for i in text:
            if i.lower() in dict_let:
                if i.isupper():
                    processed += dict_let[i.lower()].upper()
                else:
                    processed += dict_let[i]
            elif i.lower() in rev_dict:
                if i.isupper():
                    processed += rev_dict[i.lower()].upper()
                else:
                    processed += rev_dict[i]
            else:
                processed += i

        return processed

    ## The Function that asks for the user's string input
    def encrypt_decrypt():
        running = True
        while running == True:
            plaintext = input("[Encrypt/Decrypt Text]: ")
            if len(plaintext.strip()) == 0:
                print("Woops! I can't process nothingness!")
            else:
                encrypted = process(plaintext)
                print()
                print(f"The encrypted/decrypted text is: [{encrypted}]")
                print()
                running = False

    def main():
        key_create()
        print("This is the Key for the kamasutra cipher")
        print("This key changes everytime you load the program")

        print("------------------------------")
        for i in dict_let.keys():
            print(i.upper(), end=" ")
        print()
        for j in rev_dict.keys():
            print(j.upper(), end=" ")
        print()
        print("------------------------------")

        print(
            "Since the Kamasutra cipher is applicable in both directions, therefore, you can encrypt and decrypt with the Same Process"
        )
        print()
        print("It's practically similar as the monoalphabetic cipher.")
        print(
            "But if differs in the sense that instead of a complete jumbled alphabet as the key,"
        )
        print("it pairs the letters in the same alphabet set.")
        print()
        print("Pleases Select an option")
        print("1 - Encrypt/Decrypt")
        print("2 - To Exit")
        print()

        running = True
        while running == True:
            choice = input("Enter Option: ")
            if choice == "1":
                encrypt_decrypt()
            elif choice == "2":
                print("Good Bye!")
                running = False

    main()


def run_custom_cipher():
    ## This is for the key creation of the vernam cipher
    ##creates a list of letters a-z in lowercase
    low = string.ascii_lowercase
    ## Empty dictionary to be filled with the letters for the key, and their indexes in the alphabet for their values
    vern_dict = {}

    ## DIctionary for kamasutra
    dict_let = {}
    rev_dict = {}

    # functions used for displaying
    ##Function used for just displaying, not involved in encryption or decryption
    def disp(arr, desc, type):
        if type == "list":
            print(f"{desc}", end=" ")
            for i in arr:
                print(i.upper(), end=" ")
            print()
        elif type == "dict":
            print(desc, end=" ")
            for j in arr:
                j = str(vern_dict[j])
                if len(j) < 2:
                    j = "0" + j
                print(j, end=" ")
            print()

    ## displays the kamasutra
    def disp_kam(text):
        print("Performing the Kamasutra Cipher")
        text = text.strip()
        letters = []
        enc = ""
        for i in text:
            if i.isalpha():
                letters.append(i.lower())

        for j in letters:
            print(j.upper(), end=" ")
        print()

        for k in letters:
            if k in dict_let:
                enc += dict_let[k]
            elif k in rev_dict:
                enc += rev_dict[k]

        for l in enc:
            print(l.upper(), end=" ")
        print()

        ## Key Creation functions

    ## adds the letter to the dictionary as the key, and generates numbers 1-26 to be assigned as the letter's index
    def vernam_key():
        for i, low_let in zip(range(1, 27), low):
            vern_dict[low_let] = i

    ##Creates the key for the kamasutra cipher
    def kam_key():
        set1 = []
        set2 = []

        for i, let in zip(range(0, 26), low):
            if i % 2 == 1:
                set1.append(low[i])
            else:
                set2.append(low[i])

        random.shuffle(set1)
        random.shuffle(set2)

        for j, k in zip(set1, set2):
            dict_let[j] = k
            rev_dict[k] = j

            ##Functions revolving around validating the key inputs for the vernam cipher

    ## Asks the user for the key that they want to use
    ## validates tkey input
    def inp_key():
        print()
        print("***!!ENTER KEY!!***")
        print(
            "Note: Make sure that there are no numeric or special characters in the key"
        )
        print()
        running = True
        while running:
            key = input("Please enter key: ")
            if key.isalpha():
                running = False
            elif len(key.strip()) == 0:
                print()
                print("***Sorry, you can't have Nothingness as the key***")
                print()
            else:
                print()
                print(
                    "***!Your key contains something that isn't part of the alphabet. Remember: No special characters or spaces!***"
                )
                print()
        return key

    ##Checks the length of the key if it matches the length of the plain text
    def key_len(key, text):
        result = key
        index = 0

        while len(result) < len(text):
            result += key[index]
            index = (index + 1) % len(key)  # Loop back when reaching the end

        return result

        ##Functions that do the cipher algorithms

    ## The function that does the algorithm for the kamasutra cipher
    def kamasutra(text):
        processed = ""
        for i in text:
            if i.lower() in dict_let:
                if i.isupper():
                    processed += dict_let[i.lower()].lower()
                else:
                    processed += dict_let[i].upper()
            elif i.lower() in rev_dict:
                if i.isupper():
                    processed += rev_dict[i.lower()].lower()
                else:
                    processed += rev_dict[i].upper()
            else:
                processed += i

        return processed

    ## This is function that does the algorithm for the vernam cipher
    def vernam(key, plain, process):

        rev_vern = {v: k for k, v in vern_dict.items()}

        key = key.lower()
        processed = ""

        ##lists for the deconstructed string to be put ito
        brkn_strng = []
        letters = []
        processed_letters = []

        ##Each character of the plain string gets added including the spaces
        for i in plain:
            brkn_strng.append(i)

        ##This for loop separates the letters from other characters in
        for j in brkn_strng:
            if j.isalpha():
                letters.append(j.lower())

        ##Display what the key and what the plain text would look like if lined up
        print()
        print(
            "*************************************************************************"
        )
        print(f"The Key: {key}")
        print()

        if len(key) > len(letters):
            print(
                "##Woops! your key is longer than your plaintext! Think of a shorter one##"
            )
        else:
            while len(key) < len(letters):
                key = key_len(key, letters)
                print(f"The broken string is: {brkn_strng}")
                print()
                print()

            ##For encrypting, the process adds the value of the plaintext to the value of the key
            if process == "encrypt":
                print(
                    "For Encryption: The Indexes of the Plaintext and the Key is to be Added"
                )
                print(
                    "And if value is greater than 26 which is the last index, then it is to be subtracted by 26."
                )
                print()
                for k, l in zip(letters, key):

                    encrypt = vern_dict[k] + vern_dict[l]
                    ##If the result is greater than 26, then it gets subtracted by 26
                    if encrypt > 26:
                        encrypt -= 26
                    processed_letters.append(rev_vern[encrypt])

                ## To display the the operation in the numeric values
                disp(letters, "plain: ", "dict")
                disp(key, "key: + ", "dict")
                print(
                    "---------------------------------------------------------------------"
                )
                disp(processed_letters, "result:", "dict")

            ##for decrypting, the value of the encrypted text is subtracted by the value of the key
            elif process == "decrypt":
                print(
                    "For Decryption: The Indexes of the Plaintext and the Key is to be Subtracted"
                )
                print(
                    "And if value is less than or equal to 0, then 26 is to be added to the value."
                )
                print()
                for m, n in zip(letters, key):
                    decrypt = vern_dict[m] - vern_dict[n]
                    ##If the result is less than 26, then it gets added 26
                    if decrypt <= 0:
                        decrypt += 26
                    processed_letters.append(rev_vern[decrypt])

                ## To display the the operation in the numeric values
                disp(letters, "plain: ", "dict")
                disp(key, "key: - ", "dict")
                print(
                    "---------------------------------------------------------------------"
                )
                disp(processed_letters, "result:", "dict")

            counter = 0
            ##This block of code reconstructs the string back together with the encrypted letters
            for char in brkn_strng:
                if char.isalpha():
                    if char.isupper():
                        processed += processed_letters[counter].upper()
                        counter += 1
                    else:
                        processed += processed_letters[counter]
                        counter += 1
                else:
                    processed += char
            ##Explains the Process

            print()
            print()
            disp(letters, "Plain: ", "list")
            disp(key, "Key:   ", "list")
            print(
                "---------------------------------------------------------------------"
            )
            disp(processed_letters, "       ", "list")
            print()

            return processed

            ## Functions for user inputs

    ##function to be called when encrypting
    def encrypt():
        running = True
        while running == True:
            ##user input plaintext
            plain = input("[Type plain text here]: ")
            ##Calls the key_inp function
            key = inp_key()
            ##Calls the processor function
            encrypted = vernam(key, plain, "encrypt")
            disp_kam(encrypted)
            encrypted = kamasutra(encrypted)
            if encrypted == None:
                pass
            else:
                print()
                print(f"The encrypted string is [{encrypted}]")
                print()
                running = False

    ##The function to be called when decrypting
    def decrypt():
        running = True
        while running == True:
            ##user input plaintext
            encr = input("[Type encrypted text here]: ")
            ##Calls the key_inp function
            key = inp_key()
            ##Calls the processor function
            print()
            disp_kam(encr)
            encr = kamasutra(encr)
            encrypted = vernam(key, encr, "decrypt")
            if encrypted == None:
                pass
            else:
                print()
                print(f"The decrypted string is [{encrypted}]")
                print()
                running = False

    ## The main function
    def main():
        ## Function call for key creation
        vernam_key()
        kam_key()

        ## Displays the information per cipher method
        ##For vernam
        print("This is our very own cipher called: Kamasutra the Vernam")
        print("It combines the vernam cipher and the kamasutra cipher")
        print()
        print(
            "This is what the dictionary of letters and their number equivalent looks like for the vernam cipher:"
        )
        print(
            "-------------------------------------------------------------------------------------------------------------------------"
        )
        for ite, val in vern_dict.items():
            print(f"{ite.upper()}:{val}", end="|")
        print()
        print(
            "-------------------------------------------------------------------------------------------------------------------------"
        )

        ##For kamasutra
        print()
        print("And this is the key for the Kamasutra cipher:")
        disp(dict_let, "", "list")
        disp(rev_dict, "", "list")
        print()

        while True:
            print("1 - Encrypt")
            print("2 - Decrypt")
            print("3 - Exit")
            choice = input("What would you like to do?: ")
            print()

            if choice == "1":
                encrypt()
                print()

            elif choice == "2":
                decrypt()
                print()

            elif choice == "3":
                print("Good Bye!")
                break
            else:
                print("Option not found")

    main()


def run_vernam():
    ##creates a list of letters a-z in lowercase
    low = string.ascii_lowercase

    key_low = {}

    ## adds the letter to the dictionary as the key, and generates numbers 1-26 to be assigned as the letter's index
    for i, low_let in zip(range(1, 27), low):
        key_low[low_let] = i

    ## Asks the user for the key that they want to use
    ## validates tkey input
    def inp_key():
        print()
        print("***!!ENTER KEY!!***")
        print(
            "Note: Make sure that there are no numeric or special characters in the key"
        )
        print()
        running = True
        while running:
            key = input("Please enter key: ")
            if key.isalpha():
                running = False
            elif len(key.strip()) == 0:
                print()
                print("***Sorry, you can't have Nothingness as the key***")
                print()
            else:
                print()
                print(
                    "***!Your key contains something that isn't part of the alphabet. Remember: No special characters or spaces!***"
                )
                print()
        return key

    ##Checks the length of the key if it matches the length of the plain text
    def key_len(key, text):
        result = key
        index = 0

        while len(result) < len(text):
            result += key[index]
            index = (index + 1) % len(key)  # Loop back when reaching the end

        return result

    def disp(arr, desc, type):
        if type == "list":
            print(f"{desc}", end=" ")
            for i in arr:
                print(i.upper(), end=" ")
            print()
        elif type == "dict":
            for j in arr:
                j = str(key_low[j])
                if len(j) < 2:
                    j = "0" + j
                print(j, end=" ")
            print()

    ## This is function that does the encryption and decryption
    def processor(key, plain, process):

        rev_low = {v: k for k, v in key_low.items()}

        key = key.lower()
        processed = ""

        ##lists for the deconstructed string to be put ito
        brkn_strng = []
        letters = []
        processed_letters = []

        ##Each character of the plain string gets added including the spaces
        for i in plain:
            brkn_strng.append(i)

        ##This for loop separates the letters from other characters in
        for j in brkn_strng:
            if j.isalpha():
                letters.append(j.lower())

        ##Display what the key and what the plain text would look like if lined up
        print()
        print(
            "*************************************************************************"
        )
        print(f"The Key: {key}")
        print()

        if len(key) > len(letters):
            print("##Woops! your key is longer than your plaintext! Let's try again!##")
            print()
        else:
            while len(key) < len(letters):
                key = key_len(key, letters)
                print(f"The broken string is: {brkn_strng}")
                print()
                disp(letters, "Plaintext:", "list")
                disp(key, "Key:      ", "list")
                print()

            ##For encrypting, the process adds the value of the plaintext to the value of the key
            if process == "encrypt":
                print(
                    "For Encryption: The Indexes of the Plaintext and the Key is to be Added"
                )
                print(
                    "And if value is greater than 26 which is the last index, then it is to be subtracted by 26."
                )
                print()
                for k, l in zip(letters, key):
                    encrypt = key_low[k] + key_low[l]
                    ##If the result is greater than 26, then it gets subtracted by 26
                    if encrypt > 26:
                        encrypt -= 26
                    processed_letters.append(rev_low[encrypt])

            ##for decrypting, the value of the encrypted text is subtracted by the value of the key
            elif process == "decrypt":
                print(
                    "For decryption: The Indexes of the Plaintext and the Key is to be Subtracted"
                )
                print(
                    "And if value is less than or equal to 0, then 26 is to be added to the value."
                )
                print()
                for m, n in zip(letters, key):
                    decrypt = key_low[m] - key_low[n]
                    ##If the result is less than 26, then it gets added 26
                    if decrypt <= 0:
                        decrypt += 26
                    processed_letters.append(rev_low[decrypt])

            counter = 0
            ##This block of code reconstructs the string back together with the encrypted letters
            for char in brkn_strng:
                if char.isalpha():
                    if char.isupper():
                        processed += processed_letters[counter].upper()
                        counter += 1
                    else:
                        processed += processed_letters[counter]
                        counter += 1
                else:
                    processed += char
            ##Explains the Process
            disp(letters, "Plain:", "list")
            disp(key, "Key:  ", "list")

            print()
            print("This are the index values of the letters")
            print()
            disp(letters, "None", "dict")
            disp(key, "None", "dict")
            print(
                "---------------------------------------------------------------------"
            )
            disp(processed_letters, "None", "dict")
            print()
            return processed

    def encrypt():
        running = True
        while running == True:
            ##user input plaintext
            plain = input("[Type plain text here]: ")
            ##Calls the key_inp function
            key = inp_key()
            ##Calls the processor function
            encrypted = processor(key, plain, "encrypt")
            if encrypted == None:
                pass
            else:
                print()
                print(f"The encrypted string is [{encrypted}]")
                print()
                running = False

    def decrypt():
        running = True
        while running == True:
            ##user input plaintext
            plain = input("[Type encrypted text here]: ")
            ##Calls the key_inp function
            key = inp_key()
            ##Calls the processor function
            encrypted = processor(key, plain, "decrypt")
            if encrypted == None:
                pass
            else:
                print()
                print(f"The decrypted string is [{encrypted}]")
                print()
                running = False

    def main():
        print("This is the vernam cipher!")
        print()
        print(
            "This is what the dictionary of letters and their number equivalent looks like:"
        )
        print(
            "-------------------------------------------------------------------------------------------------------------------------"
        )
        for ite, val in key_low.items():
            print(f"{ite.upper()}:{val}", end="|")
        print()
        print(
            "-------------------------------------------------------------------------------------------------------------------------"
        )

        while True:
            print("1 - Encrypt")
            print("2 - Decrypt")
            print("3 - Exit")
            choice = input("What would you like to do?: ")
            print()

            if choice == "1":
                encrypt()
                print()

            elif choice == "2":
                decrypt()
                print()

            elif choice == "3":
                print("Good Bye!")
                break
            else:
                print("Option not found")

    main()


def run_mono():
    letters = list(string.ascii_lowercase)

    ##Shuffled letters for encryption
    shuffled = letters[:]  # Creates a copy of the letters list
    random.shuffle(shuffled)

    ##Empty dictionary for key creation
    key = {}
    key_num = {}
    ##Create key

    def letter_key():
        for i, j in zip(letters, shuffled):
            key[i] = j

    def number_key():
        shuf_num = list(range(10))
        random.shuffle(shuf_num)

        for i, j in zip(range(0, 10), shuf_num):
            key_num[str(i)] = str(j)

    ##Function to display the plaintext and the key text
    def display(key):
        print("Plain: ", end=" ")
        for i in key:
            print(i.upper(), end=" ")

        print()

        print("Key:   ", end=" ")
        for j in key:
            print(key[j].upper(), end=" ")

        print()
        print()

    def process(text, type):
        rev_key = {v: k for k, v in key.items()}
        rev_key_num = {v: k for k, v in key_num.items()}

        processed = ""

        if type == "encrypt":
            print()
            for i in text:
                if i.lower() in key:
                    if i.isupper():
                        processed += key[i.lower()].upper()
                    else:
                        processed += key[i]

                elif i in key_num:
                    processed += key_num[i]
                else:
                    processed += i

        elif type == "decrypt":
            for j in text:
                if j.lower() in rev_key:
                    if j.isupper():
                        processed += rev_key[j.lower()].upper()
                    else:
                        processed += rev_key[j]

                elif j in rev_key_num:
                    processed += rev_key_num[j]
                else:
                    processed += j

        return processed

    def encrypt():
        print()
        print("**!!You are encrypting!!**")
        running = True
        while running == True:
            text = input("[Enter your Plaintext Here]: ")
            if len(text.strip()) == 0:
                print("I Can't Encrypt nothingness")
            else:
                encrypted = process(text, "encrypt")
                print(f"Your encrypted text is: {[encrypted]}")
                running = False

    def decrypt():
        print()
        print("**!!You are decrypting!!**")
        running = True
        while running == True:
            text = input("[Enter your Encrypted Text Here]: ")
            if len(text.strip()) == 0:
                print("I Can't decrypt nothingness")
            else:
                decrypted = process(text, "decrypt")
                print()
                print(f"Your decrypted text is: {[decrypted]}")
                running = False

    def main():
        print("This is the Monoalphabetic cipher:")
        letter_key()
        number_key()

        print("This is the key for the letters:")
        display(key)
        print("This is the key for the numbers:")
        display(key_num)
        print()

        print("1 - Encrypt")
        print("2 - Decrypt")
        print("3 - Exit ")

        running = True

        while running == True:
            print()
            choice = input("Enter your choice: ")
            if choice == "1":
                encrypt()
            elif choice == "2":
                decrypt()
            elif choice == "3":
                print("Good Bye!")
                running = False
            else:
                print("Sorry, but your choice is not on the options")

        ##To display the plain text and its equivalent key

    main()


if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(script_dir)
    manager = CipherManager()
    manager.run()

