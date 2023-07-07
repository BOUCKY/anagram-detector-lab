class Anagram:
    
    def __init__(self, word):
        self.word = word

    def match(self, list_of_words):
        anagrams = []
        sorted_word = sorted(self.word)

        for w in list_of_words:
            if w.lower() != self.word and sorted(w.lower()) == sorted_word:
                anagrams.append(w)

        return anagrams