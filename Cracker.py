#!/usr/bin/env python3

class Cracker:
    def __init__(self, alphabet, rotation):
        if rotation.upper() == "RIGHT":
            self.rotate_right = True
        else:
            raise ValueError("Rotation value is not allowed")
        self.alphabet = alphabet

        #Calculate the two halves of alphabet:
        self.alpha_first, self.alpha_last = [],[]

        for letter in self.alphabet[:len(self.alphabet)//2]:
            self.alpha_first.append(letter)

        for letter in self.alphabet[len(self.alphabet)//2:]:
            self.alpha_last.append(letter)

        # Create Dictionary
        self.dictionary = {}

        for letra in range(len(self.alphabet)):
            new_last = self.alpha_last[-(letra//2):] + self.alpha_last[:-(letra//2)]
            self.dictionary[self.alphabet[letra]] = [self.alpha_first,new_last]


    def __clean_text(self, text):
        text_new = ""
        # First we remove spaces
        for word in text.split(" "):
            text_new += word

        text = ""
        # And then, we remove breaklines
        for word in text_new.split("\n"):
            text += word
        return text

    def __create_pattern(self, text):
        word_pattern = ""
        for letter in text:
            if letter in self.alpha_first:
                word_pattern += str(0)
            elif letter in self.alpha_last:
                word_pattern += str(1)
            else:
                print("Unexpected Error")
                return

        return word_pattern

    def __invert_pattern(self, pattern):
        new_pattern = ""
        for num in pattern:
            if num == "0":
                new_pattern += "1"
            else:
                new_pattern += "0"
        return new_pattern

    def __find_matches(self, encrypted_text, known_text):
        # Search for a coincident match
        patt_encrypt = self.__create_pattern(encrypted_text)
        # The theory pattern should be inverted
        patt_theory = self.__create_pattern(known_text)
        matches = patt_encrypt.split(self.__invert_pattern(patt_theory))
        results = []
        for match in matches:
            results.append(len(match))
        return results

    def find_match(self, encrypted_text, known_word):
        place = self.__find_matches(encrypted_text, known_word)
        return encrypted_text[place[0]:place[0]+len(known_word)]

    # Give two words with both the same lenght. Text independent
    def extract_dictionary(self, encrypted_word, theory_word):
        possible_key = []
        for char in range(len(theory_word)):
            pair = [] #Because the key has two letters for the same alphabet
            if theory_word[char] in self.alpha_first:
                for table in self.dictionary:
                    indice = self.dictionary[table][1].index(encrypted_word[char])
                    if self.dictionary[table][0][indice] is theory_word[char]:
                        pair.append(table)

            elif theory_word[char] in self.alpha_last:
                for table in self.dictionary:
                    lett = self.dictionary[table][1].index(theory_word[char])
                    if self.dictionary[table][0][lett] is encrypted_word[char]:
                        pair.append(table)
            else:
                pair.append(NULL)
            possible_key.append(set(pair))

        return possible_key
    def match_keys(self, keys):
        key = []

    def crack_code(self, encrypted_text, known_words):
        keys = []
        for known_word in known_words:
            coded_word = self.find_match(self.__clean_text(encrypted_text), known_word)
            keys.append(self.extract_dictionary(coded_word, known_word))

        return keys
