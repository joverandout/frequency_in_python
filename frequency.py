class Freq:
    def __init__(self,file):
        with open(file, "rt") as f:
            self.text = f.read()

        self.analysis = list([0,chr(i+65)] for i in range(0,26))

        for char in self.text.upper():
            if ord(char) in range(65,92):
                self.analysis[ord(char)-65][0] += 1

    def __str__(self):
        out_string = ""
        for i in range(0,26):
            out_string += str(self.analysis[i][1]) + ": " + str(self.analysis[i][0]) + "\n"
        return out_string

    def ordered(self):
        self.analysis.sort(key=lambda x:x[0], reverse=True)
        out_string = self.__str__()
        self.analysis.sort(key=lambda x:x[1])
        return out_string
