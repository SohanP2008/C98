def countWordsFromFile():
    fileName = input("Enter the path of the file: ")
    file = open(fileName, 'r')
    numberOfWords = 0
    for i in file:
        words = i.split()
        numberOfWords = numberOfWords + len(words)
    print("The number of words: ", numberOfWords)
countWordsFromFile()