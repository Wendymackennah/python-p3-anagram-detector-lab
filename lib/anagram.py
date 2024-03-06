# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()  # Convert to lowercase for case-insensitive comparison

    def match(self, possible_anagrams):
        matches = []
        for possible_anagram in possible_anagrams:
            if self._is_anagram(possible_anagram.lower()):
                matches.append(possible_anagram)
        return matches

    def _is_anagram(self, possible_anagram):
        # Check if the letters of possible_anagram are the same as self.word
        return sorted(possible_anagram) == sorted(self.word)
