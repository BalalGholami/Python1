# Personal Data Structure

# mesal:
# yek sanad darim ke tedadi kalame darad. mikhahim tedad kalame haaye in document
# ra mohasebe konim.

class BagOfWord:
    def __init__(self):
        self.words = {}

    def add(self, word):
        self.words[word.lower()] = self.words.get(word.lower(), 0) + 1

    def __getitem__(self, word):
        return self.words.get(word.lower(), 0)

    def __setitem__(self, word, count):
        self.words[word.lower()] = count

    def __len__(self):
        return len(self.words)

    def __iter__(self):  # object maa raa "iterable" mikonad
        return iter(self.words)


document = BagOfWord()
document.add("Python")
document.add("Python")
document.add("python")
print(document.words)
# tekrar in kalameye khas ra hesab mikonad. magic method=getitem
print(document["Python"])
document["Python"] = 10  # magic method: set item
print(document["Python"])  # tekrar in kalameye khas ra hesab mikonad
print(len(document))  # tedad kalame ha ra migooyad. magic method: len

print(document.__dict__)
