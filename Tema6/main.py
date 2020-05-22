import os


class GenericFile:
    def get_path(self):
        pass

    def get_freq(self):
        pass


class TextASCII(GenericFile):
    def __init__(self, path, fr):
        self.path_absolute = path
        self.frecvente = fr

    def get_freq(self):
        return self.frecvente

    def get_path(self):
        return self.path_absolute

    def __repr__(self):
        return self.path_absolute


class TextUNICODE(GenericFile):
    def __init__(self, path, fr):
        self.path_absolute=path
        self.frecvente = fr

    def get_freq(self):
        return self.frecvente

    def get_path(self):
        return self.path_absolute

    def __repr__(self):
        return self.path_absolute


class Binary(GenericFile):
    def __init__(self, path, fr):
        self.path_absolute = path
        self.frecvente = fr

    def get_freq(self):
        return self.frecvente

    def get_path(self):
        return self.path_absolute

    def __repr__(self):
        return self.path_absolute


def detectTYPE(content, path):

    nr_caractere = 0
    frecventa = [0]*255


    #calcul frecventa caracter si nr caractere
    for c in content:
        frecventa[ord(c)] += 1
        nr_caractere += 1

    # verificare text ASCII

    frecventa_caractere = frecventa[int("9")] + frecventa[int("10")] + frecventa[int("13")]

    for c in range(32, 127):
        frecventa_caractere += frecventa[int(str(c))]

    if frecventa_caractere / nr_caractere >= 0.8:
        return TextASCII(path, frecventa)

    #verificare text UNICODE  => frecventa lui 0 apare cel putin in 30% din text

    if frecventa[ord("0")] / nr_caractere >= 0.3:
        return TextUNICODE(path, frecventa)

    #in caz ca nu este nici ASCII nici UNICODE returnam BINARY

    return Binary(path, frecventa)


if __name__ == "__main__":

    _files = []
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    for root, subdirs, files in os.walk(ROOT_DIR):
        for file in os.listdir(root):
            if file.endswith("txt"):
                file_path = os.path.join(root, file)
                if os.path.isfile(file_path):
                    f = open(file_path, 'rb')
                    try:
                        content = f.read()
                        _files.append(detectTYPE(content, file_path))
                    finally:
                        f.close()
    i = 1
    for file in _files:
        print("Fisier " + i + ": " + file)
        i+=1