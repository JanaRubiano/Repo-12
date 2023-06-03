'''
Return the number of consonants in a text.
'''
def countConsonants(text:str) -> int:
    consonants = 0
    for x in text:
        if x.isalpha() and x not in "AEIOUaeiou":
            consonants += 1
    return consonants

if __name__ == "__main__":
    with open("mbox-short.txt", "r") as file:
        print(f"There are {countConsonants(file.read())} of consonants in the file.")

