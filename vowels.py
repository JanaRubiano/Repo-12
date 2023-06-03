'''
Return the number of vowels in a text.
'''
def countVowels(text:str) -> int:
    vowels = 0
    for char in text:
        if char in "AEIOUaeiou":
            vowels += 1
    return vowels

if __name__ == "__main__":
    with open("mbox-short.txt", "r") as file:
        print(f"There are {countVowels(file.read())} of vowels in the file.")