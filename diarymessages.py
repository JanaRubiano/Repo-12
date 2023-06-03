'''
Number of sent messages each day.
'''
def diaryMessage(text:str) -> list:
    received_ms = [] # List of segments of the text that contain the date information.
    words = text.split() # List of strings of each word in text.
    for i in range(len(words)): # Block of code to separate segments.
        if words[i] == "Received:": # A list of strings is created from the word "Received to the word "(GMT)" or "-0500".
            segment = []
            while words[i] != "-0500" and words[i] != "(GMT)":
                segment.append(words[i])
                i += 1
            received_ms.append(segment)
    
    m_per_day = {} # A dict is created to store day and number of sent messages.
    for i in range(len(received_ms)):
        ind = received_ms[i].index('Jan') # Index of the word "Jan".
        day = int(received_ms[i][ind - 1]) # Day is extracted bassed on the index of "Jan".
        if day in m_per_day: # Block of code to fill de dict.
            m_per_day[day] += 1
        else:
            m_per_day[day] = 1

    return m_per_day

if __name__ == "__main__":
    with open("mbox-short.txt", "r") as file:
        day_num = diaryMessage(file.read())
        for day in day_num:
            print(f"{day_num[day]} messages were sent on January {day}, 2008")