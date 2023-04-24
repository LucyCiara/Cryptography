
alphabets = [[0, "a", "000000", "A"], [1, "b", "000001", "B"], [2, "c", "000010", "C"], [3, "d", "000011", "D"], [4, "e", "000100", "E"], [5, "f", "000101", "F"], [6, "g", "000110", "G"], [7, "h", "000111", "H"], [8, "i", "001000", "I"], [9, "j", "001001", "J"], [10, "k", "001010", "K"], [11, "l", "001011", "L"], [12, "m", "001100", "M"], [13, "n", "001101", "N"], [14, "o", "001110", "O"], [15, "p", "001111", "P"], [16, "q", "010000", "Q"], [17, "r", "010001", "R"], [18, "s", "010010", "S"], [19, "t", "010011", "T"], [20, "u", "010100", "U"], [21, "v", "010101", "V"], [22, "w", "010110", "W"], [23, "x", "010111", "X"], [24, "y", "011000", "Y"], [25, "z", "011001", "Z"], [26, "æ", "011010", "Æ"], [27, "ø", "011011", "Ø"], [28, "å", "011100", "Å"], [29, " ", "011101", ""], [30, ",", "011110", ""], [31, ".", "011111", ""],
[32, "1", "100000", ""], [33, "2", "100001", ""], [34, "3", "100010", ""], [35, "4", "100011", ""], [36, "5", "100100", ""], [37, "6", "100101", ""], [38, "7", "100110", ""], [39, "8", "100111", ""], [40, "9", "101000", ""], [41, "?", "101001", ""], [42, "!", "101010", ""], [43, '"', "101011", ""], [44, "/", "101100", ""], [45, "(", "101101", ""], [46, ")", "101110", ""], [47, "=", "101111", ""], [48, "+", "110000", ""], [49, "-", "110001", ""], [50, "<", "110010", ""], [51, ">", "110011", ""], [52, "#", "110100", ""], [53, "$", "110101", ""], [54, "%", "110110", ""], [55, "&", "110111", ""], [56, "'", "111000", ""], [57, "*", "111001", ""], [58, "~", "111010", ""], [59, "^", "111011", ""], [60, "_", "111100", ""], [61, ":", "111101", ""], [62, ";", "111110", ""], [63, "@", "111111", ""]]
SBoxAlphabets = [[30, ",", "011110", ""], [6, "g", "000110", "G"], [37, "6", "100101", ""], [20, "u", "010100", "U"], [60, "_", "111100", ""], [25, "z", "011001", "Z"], [43, '"', "101011", ""], [27, "ø", "011011", "Ø"], [48, "+", "110000", ""], [19, "t", "010011", "T"], [47, "=", "101111", ""], [55, "&", "110111", ""], [17, "r", "010001", "R"], [32, "1", "100000", ""], [53, "$", "110101", ""], [18, "s", "010010", "S"], [54, "%", "110110", ""], [59, "^", "111011", ""], [8, "i", "001000", "I"], [14, "o", "001110", "O"], [57, "*", "111001", ""], [38, "7", "100110", ""], [1, "b", "000001", "B"], [9, "j", "001001", "J"], [2, "c", "000010", "C"], [39, "8", "100111", ""], [33, "2", "100001", ""], [61, ":", "111101", ""], [23, "x", "010111", "X"], [42, "!", "101010", ""], [0, "a", "000000", "A"], [44, "/", "101100", ""],
[15, "p", "001111", "P"], [28, "å", "011100", "Å"], [11, "l", "001011", "L"], [52, "#", "110100", ""], [41, "?", "101001", ""], [29, " ", "011101", ""], [3, "d", "000011", "D"], [13, "n", "001101", "N"], [31, ".", "011111", ""], [50, "<", "110010", ""], [4, "e", "000100", "E"], [26, "æ", "011010", "Æ"], [7, "h", "000111", "H"], [62, ";", "111110", ""], [51, ">", "110011", ""], [10, "k", "001010", "K"], [35, "4", "100011", ""], [12, "m", "001100", "M"], [63, "@", "111111", ""], [21, "v", "010101", "V"], [24, "y", "011000", "Y"], [40, "9", "101000", ""], [56, "'", "111000", ""], [58, "~", "111010", ""], [34, "3", "100010", ""], [46, ")", "101110", ""], [16, "q", "010000", "Q"], [45, "(", "101101", ""], [49, "-", "110001", ""], [5, "f", "000101", "F"], [36, "5", "100100", ""], [22, "w", "010110", "W"]]
run = True

word = ""
wordList = []

keyStr = ""
keyList = []

convertStr = ""
convertList = []

deconvertList = []

shuffleStr = ""
shuffleList = []

tempList = []
tempList2 = []

actiVarsList = [keyList, wordList, shuffleList, convertList, deconvertList]
actiVarsStr = [word, keyStr, shuffleStr, convertStr]

def varRe():
    global word, keyStr, keyList, wordList, shuffleStr, shuffleList, convertList, convertStr, reconvertList, deshuffleList, deshuffleStr
    #   Resets all variables
    keyList.clear(), wordList.clear(), shuffleList.clear(), convertList.clear(), deconvertList.clear()
    shuffleStr, convertStr = "", ""

def prep():
    global word, keyStr, shuffleStr, convertStr, deshuffleStr, keyList, wordList, shuffleList, convertList, reconvertList, deshuffleList
    #   Prepares the message for shuffling by making sure it's
    #   divisible by 6, adding a space at the end of the message
    #   so it adds up.
    while len(word)%6 != 0:
        word += " "
    #   Adds the corresponding nested list in the alphabets list
    #   for each letter in the message.
    for i in range (0, len(word)):
        for x in alphabets:
            if x[1] == word[i] or (x[3] == word[i] and x[3] != ""):
                wordList.append(x)
    #   Adds the corresponding nested list in the alphabets list
    #   for each letter in the key, and repeats the key until it's
    #   the length of the message.
    for i in range (len(word)-len(keyStr)):
        keyStr += keyStr[i]
    for i in range (0, len(keyStr)):
        for x in alphabets:
            if x[1] == keyStr[i] or (x[3] == keyStr[i] and x[3] != ""):
                keyList.append(x)

def shuffle():
    global shuffleList, word, keyStr, shuffleStr
    #   Shuffles the message,

    #       abcdef ghijkl mnopqr stuvw xyzæøå 123456
    #       =>
    #       agmsx1 bhnty2 ciouz3 djpuæ4 ekqvø5 flrwå6

    #   and adds the shuffled message to a new list. Works the same
    #   when encrypting and decrypting.
    for i in range(0, len(word), 6):
        for x in range(6):
            tempList.append(wordList[i+x])
        for a in range(6):
            for f in range(6):
                tempList2.append(tempList[f][2][a])
            for y in alphabets:
                if y[2] == "".join(tempList2):
                    shuffleList.append(y)
            tempList2.clear()
        tempList.clear()

def crypV():
    global convertStr
    #   Uses vigenère cipher to encrypt the message, and outputs
    #   it to a string.
    for i in range (len(shuffleList)):
        if shuffleList[i][0] + keyList[i][0] < 64:
            for x in alphabets:
                if shuffleList[i][0] + keyList[i][0] == x[0]:
                    convertStr += x[1]
        else:
            for x in alphabets:
                if shuffleList[i][0] + keyList[i][0] - 64 == x[0]:
                    convertStr += x[1]

def decrypV():
    global deconvertList, word, wordList
    #   Uses vigenère cipher to decrypt the message, and outputs
    #   it to the list wordList.
    for i in range (len(wordList)):
        if wordList[i][0] - keyList[i][0] >= 0:
            for x in alphabets:
                if wordList[i][0] - keyList[i][0] == x[0]:
                    deconvertList.append(x[1])
        else:
            for x in alphabets:
                if wordList[i][0] - keyList[i][0] + 64 == x[0]:
                    deconvertList.append(x[1])
    word = "".join(deconvertList)
    deconvertList.clear()
    wordList.clear()
    for i in range(len(word)):
        for x in alphabets:
            if x[1] == word[i]:
                wordList.append(x)

def Sboxing():
    global word, wordList
    #   Uses S-boxing to give binary values new binary values using
    #   the S-box I created.
    for i in range(len(wordList)):
        for x in range(len(alphabets)):
            if alphabets[x] == wordList[i]:
                tempList.append(SBoxAlphabets[x])
    wordList = tempList.copy()
    tempList.clear()

def unSboxing():
    global shuffleStr, shuffleList
    #   Converts from the S-box values to the original values.
    for i in range(len(shuffleList)):
        for x in range(len(SBoxAlphabets)):
            if SBoxAlphabets[x] == shuffleList[i]:
                tempList.append(alphabets[x])
    shuffleList = tempList.copy()
    for i in range(len(shuffleList)):
        shuffleStr += shuffleList[i][1]
    tempList.clear()

def cryptProc():
    global word, keyStr
    #   Runs the encryption process in order.
    varRe()
    prep()
    Sboxing()
    shuffle()
    crypV()
    
    word = convertStr

def decryptProc():
    global word, keyStr
    #   Runs the decryption process in order.
    varRe()
    prep()
    decrypV()
    shuffle()
    unSboxing()
    
    word = shuffleStr

print("Crypt ver 22")

while run == True:
    #   A user interface for the program.
    varRe()
    print()
    print("1:   Encrypt")
    print("2:   Decrypt")
    mode = input("")
    print()
    if mode == "1":
        print("Write the message you want encrypted")
        word = input("")
        print()
        print("Write the key you want to encrypt with")
        keyStr = input("")
        for i in range(16):
            cryptProc()
        print("Encrypted:", word)
    elif mode == "2":
        print("Write the message you want to decrypt")
        word = input("")
        print()
        print("Write the key you want to decrypt with")
        keyStr = input("")    
        print()
        for i in range(16):
            decryptProc()
        print("Decrypted:", word)
    else:
        print("Input must be 1 or 2")
    print()
    print("1:   Continue")
    print("2:   Quit")
    speedster = input()
    if speedster == "1":
        pass
    else:
        run = False