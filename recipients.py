'''
List of recipients with number of received messages.
'''
def recipients(text:str) -> dict:
    words = text.split() # Create a list of strings with every word in the text.
    rcpnts = {} # Dict that's going to contain email of recipient and number of received messages.
    for i in range(len(words)):
        if (words[i] == "by" or words[i] == "BY") and "." in words[i-1]: # The string that's infront of by/BY and contains a dot is the email of a recipient.
            if words[i+1] in rcpnts: # Block of code to fill de dict.
                rcpnts[words[i+1]] += 1
            else:
                rcpnts[words[i+1]] = 1  

    listado = list(rcpnts.items()) # List of tups with recipient and number of received messages.

    return listado
    
    
if __name__ == "__main__":
    with open("mbox-short.txt", "r") as file:
        name_num = recipients(file.read())
        for i in range(len(name_num)):
            lenstr = len(name_num[i])
            print(*name_num[i], sep=(5*" "),end="\n")