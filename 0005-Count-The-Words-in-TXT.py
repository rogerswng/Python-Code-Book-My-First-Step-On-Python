class counterOfWords():
    def __init__(self):
        self.words = None
        self.file = None

    def openFile(self, path):
        self.file = open(path, "r")
        return True
    def countTheWords(self):
        self.words = {}
        for each_line in self.file:
            for word in each_line.lower().split():
                word = word.strip()
                self.words[word] = self.words.get(word, 0)+1
        return True
    def printTheDict(self, str):
        self.file = open(str, "w")
        for word in sorted(self.words):
            self.file.write("{0} occurs {1} time(s).\n".format(word, self.words[word]))
        self.file.close()
        return True

#FOLLOWING TESTS
test = counterOfWords()
test.openFile("test.txt")
test.countTheWords()
test.printTheDict("Dict.txt")

        
