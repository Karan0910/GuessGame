def readFile():
    wordArray=[]
    with open("four_letters.txt", "r") as f:
        for line in f:
            inner_list = [elt.strip() for elt in line.split(' ')]
            for i in range(len(inner_list)):
                wordArray.append(inner_list[i])
        return wordArray