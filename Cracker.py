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
        
        
    def crack_code(self,encrypted_text, known_word):
        None

x = Cracker("Hello","RIGHT");
