'''
Returns the 50 most frequent words in a text.
'''
def countFiftyFrequentWords(text:str) -> list:
    
    words = text.split() # A list is created from the text, separing the words by whitespace or newline.
    for i in range(len(words)): # A loop is made to delete characters that are not part of the actual word.
        if not words[i].isalpha(): # If the word is not completely an alphabetic character then:
            new = words[i].strip(",;.:-_") # Punctuation signs are deleted.
            words.pop(i) # The word is replaced with the striped version.
            words.insert(i, new)

    
    
    # Create a dictionary with word as key an occurance as value.
    ord_words = {}
    for word in words:
        if word in ord_words and word.isalpha():
            ord_words[word] += 1
        elif word not in ord_words and word.isalpha():
            ord_words[word] = 1

    
    ord_words2 = [list(ord_words.items())[i][::-1] for i in range(len(ord_words))] # Reverse the set created by .items() so then it can be sorted by value.
    freq_words = sorted(ord_words2, reverse=True)[:50] # Sort the fifty most frequent words.
    words_50 = [freq_words[i][1] for i in range(len(freq_words))] # Creates a list with only the words.


    return words_50

if __name__ == "__main__":
    with open("mbox-short.txt", "r") as file:
        print(*countFiftyFrequentWords(file.read()), sep='\n')

